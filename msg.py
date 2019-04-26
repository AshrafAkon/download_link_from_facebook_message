from fbchat import Client
from fbchat.models import *
import xmlrpc.client as rpc
import requests
import time
import urllib.parse
import random
from settigs import group_id, email_id, id_password, file_path, log_file, rpc_url, key
from settings import who_sent
                                    
#################

#global_variables
new_msg = []
old_msg = []
unique_req = []
allowed_arg = ['link', 'torrent', 'meta']
grp_chat_id = group_id 
i = 1
####end
with open(file_path, "w") as f:
    file.read()
with open(log_file, "w") as f:
    file.read()

    
def start_down(file_type, data, author):
    if file_type == 'link' or file_type == 'meta':
        gid = server.aria2.addUri(key,[data])
        name = server.aria2.tellStatus(key, gid)['files'][0]['path'].split("/")[-1]
        confirmed_text = f"Your download has started with the file name {name}"
        client.send(Message(text=confirmed_text), thread_id=author, thread_type=ThreadType.USER)
        down_started = f"download started from {who_sent(author)} with the file name {name}"
        with open(log_file, 'a') as log:
            log.write(down_started) 
        print(down_started)
       
    elif file_type == 'torrent':

        url = urllib.parse.unquote(data).split("php?u=")[1]
        fil = requests.get(url).content
        #print(fil)
        gid = server.aria2.addTorrent(key, rpc.Binary(fil))
        name = server.aria2.tellStatus(key, gid)['files'][0]['path'].split("/")[-1]
        confirmed_text = f"You download has started with the file name {name}"
        client.send(Message(text=confirmed_text), thread_id=author, thread_type=ThreadType.USER)
        down_started = f"download started from {who_sent(author)} with the file name {name}"
        with open(log_file, 'a') as log:
            log.write(down_started)
        print(down_started)
    else:
        print("not a valid data type")

def torrent_file(message): #a message object will be supplied and it will return the url of the file
    attachment = message.attachments[0]
    if isinstance(attachment, FileAttachment): #check if its file
        url = attachment.url #fetching the url
        file_name = attachment.name
    return url, file_name 

"""this function bellow(split_uid_msg) receives a message object and then return a list in this format [uid, [file_type, link or torrent_file_url]] """      
def split_uid_msg(message): 
    uid = message.uid
    text_msg = message.text.split(' ')
    #file_type, text_msg = message.text.split(' ')
        
    if len(text_msg) == 2 or message.attachments:
        if len(text_msg) == 1 and len(message.attachments) == 1:  
            link, name = torrent_file(message)
            print(name)
            return [uid, 'torrent' , link, message.author]
        
        else:
            #file_type, text_msg = message.text.split(' ')
            print(text_msg[0])
            return [uid, text_msg[0], text_msg[1], message.author]
    else:
        pass
        


    

def unique_requests(list1): 
    #list1 = new list of data fetched from messages, list2 = old data
    simple_list = []
    final_list = []
    list2 = []
    with open(file_path, 'r') as f:
        x = f.read()
    y = x.split('&&&7_7&&&')
    y.pop()
    for z in y:
        list2.append(z.split('%%%5_5%%%'))
    
    if len(list2) > 0:
        for curr in list2:
            simple_list.append(curr[0])
    
    for i in list1:
        if i[0] in simple_list:
            pass
        else:
            final_list.append(i)
        
    if len(final_list) > 0:    
        with open(file_path, 'a') as f:
            for i in final_list:
                for n in i:
                    f.write(n)
                    f.write('%%%5_5%%%')
                f.write('&&&7_7&&&')
    return final_list
#logging to user
client = Client(email_id, id_password)
while True:
    print(f"\n\n\n\n\n\n\nnew session. session number {i}")
    last_ten_msg = client.fetchThreadMessages(thread_id=grp_chat_id, limit=10)
    
    if len(last_ten_msg) > 0:
        print("new req")
        for current_msg in last_ten_msg: #storing the messages in a organized way
            if current_msg.text == None:
                pass
            elif current_msg.attachments:
                new_msg.append(split_uid_msg(current_msg))
                
            elif split_uid_msg(current_msg) == None:
                pass

            else:
                new_msg.append(split_uid_msg(current_msg))
    
        print("\n\n\n")
        print(f"new msg = {new_msg}")
        unique_req = unique_requests(new_msg)
        print(f"unique req = {unique_req}")
        if len(unique_req) > 0:
            for download in unique_req:
                print(download[1], download[2], download[3])
                start_down(download[1], download[2], download[3])
            #old_msg = []
            #old_msg = unique_req
        else:
            print(f"nothing to download on session {i}")
            

        #if len(unique_re
        #old_msg = []
        #old_msg = unique_req
        last_ten_msg = []
        new_msg = []
        unique_req = []
    
        print(f"{i} session finished")
    
        time.sleep(90)
    else:
        time.sleep(60)
    i += 1
