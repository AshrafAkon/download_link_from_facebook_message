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

Caution : use this code at your own risk. This code is serves to "As-is" basis. 
Licence = MIT Licence
