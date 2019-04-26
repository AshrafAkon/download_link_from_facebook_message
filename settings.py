#make sure that all the variables are a string
group_id = "55845663225486" #copy the group chat Id form facebook. every group has a unique code


#provide email id and password bellow as string
email_id = "abc@example.com"
password = "examplepass"

file_path = "vari.txt" #This program uses this file to storage variables. It is important to define this. Otherwise code will not work.
log_file = "log.txt" #This file is used to write logs. If a download is started it will input an entry to the file. 

rpc_url = "example_ip.rpc" #provide the link of your aria2 server. you have to enable rpc protocol on aria2 config. 
rpc_key = "your secret rpc key" #this is the token that is used to authenticate with the aria2 rpc server. I highly suggest you to use tokens. If you dont want to use tokens you have to change some of the codes. 

#below you have to provide the user list. that are gonna send messages. you can add as much as you like. just add a "elif" statement and you should be good to go
"""this function who_Sent returns who sent the message to you. there are other ways to do it with the fbchat module. but I hard coded it. as I was using this code for personal use.""" 

def who_sent(user_id):
    if user_id == "557889878755": 
        return 'Name1'
    elif user_id == "44548799545133":
        return 'Name2'
    elif user_id == '544474444752557':
        return 'name3'

#in order to make the script work you need a rpc enabled aria2 installed machine
#this was my personal code to solve a problem. Hope it helps
