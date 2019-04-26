# download_link_from_facebook_message
If you send a link to a Facebook Id that is logged in to your script. The script will download the file or torrent.

#### It needs id and password of an account. and then a unique code of facebook convo(group or personal)
#### If someone send link in this format "link https://example.com/ex.zip". it will get the link and start downloading to the remote aria2 server
#### This code can be modified for other purposes
#### It needs aria2 security token
#### It can download torrent from magnet link or if the .torrent file is sent

## For this code to work. you have to install the following python packages with pip
```python
pip install fbchat
pip install xmlrpc
pip install urllib
```
Make sure to replace "pip" with pip3 in linux any linux distro.
I tested this code in windows. This should work just fine in any debian based or other linux distros. 
I didnt updated the code in a long time. There is a chance that this code wont work out of the box. But with some previous python experience you should be able to get this to a working condition. In that case please open a issue so I can change the code to updated condition. You can also fork it. 

Before you run the code you fist have to open "settings.py" and set your facebook email and password. I recommend you open a separate account for this. And then you will the "rpc token" from aria2 server. this code uses aria2 for downloading the files and torrents. so you first have to know how to use aria2 downloader and how to use the rpc protocol

This code created a "var.txt" and "log.txt" in the current directory. 
Make use to define the user id's in the settings.py 
Otherwise it will throw a error. you can also use the code without it. But you have to eliminate the need to ideantify the user. 
#### I wrote this code years ago. So the algorithms I used here are not even close to saying good. Pardon me
Caution : use this code at your own risk. This code is served to "As-is" basis. No warrenty of any kind is provided 
Licence = MIT Licence
