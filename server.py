# coding=utf-8
'''
Mukioplayer_Py_Mac 2.000.11
Based on Mukioplayer
MIT licence
Beining@ACICFG
cnbeining[at]gmail.com
'''
import thread
import random
import os
from os.path import expanduser
import getpass
import sys
import webbrowser
from multiprocessing import Process
import urllib
import threading
import shutil


reload(sys)
sys.setdefaultencoding('utf-8')
#try to fix the damn code problem

port = str(random.randint(6000, 15000))

def http_server():
    py_path = sys.path[0]
    real_path = getrelpath(py_path)
    os.chdir(py_path)
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from SocketServer import ThreadingMixIn
    class ThreadingServer(ThreadingMixIn,HTTPServer):
        pass
    serveraddr=('', int(port))   # http://yige.org
    srvr=ThreadingServer(serveraddr,SimpleHTTPRequestHandler)
    srvr.serve_forever()




def getrelpath(input_file):
    '''Good with all *nix.'''
    user = getpass.getuser()
    user_dir = expanduser("~")
    os.chdir(user_dir)
    file_relpath = os.path.relpath(input_file)
    return file_relpath


def main(video_relpath, danmu_relpath):
    #danmu_relpath = getrelpath(danmu_relpath)
    #video_relpath = getrelpath(video_relpath)
    if danmu_relpath is '':
        danmu_relpath = video_relpath.split('.')[:-1][0] + '.xml'
    video_filename = video_relpath.split("/")[-1]
    print(video_filename.split('.')[0])
    danmu_filename = danmu_relpath.split("/")[-1]
    py_path = sys.path[0]
    os.chdir(py_path)
    user_dir = expanduser("~")
    #print(user_dir)
    try:
        os.system('mkdir '+user_dir+'/.cache/')
    except:
        pass
    real_cache_dir = user_dir + '/.cache/mukioplayer_py'
    os.system('rm -rf /'+real_cache_dir)
    os.system('mkdir /'+real_cache_dir)
    os.chdir(py_path)
    os.system('rm -rf ./mukiocache')
    os.system('mkdir mukiocache')
    os.system('ln -s '+ real_cache_dir+' ./mukiocache ')
    os.system('cp /'+ video_relpath+'  '+ real_cache_dir)
    os.system('cp /'+ danmu_relpath+'  '+ real_cache_dir)
    video_newfilename = video_filename.replace('\\', '').replace('#', '')
    os.system('mv '+real_cache_dir+'/'+danmu_filename +' '+real_cache_dir+'/danmu.xml')
    os.system('mv '+real_cache_dir+'/'+video_filename +' '+real_cache_dir+'/'+video_newfilename)
    #fix the problem that video_filename cannot have '#' in it
    xml_to_write = '''<?xml version="1.0" encoding="utf-8"?>
<conf>
  <performance>
    <maxwidth>2048</maxwidth>
    <maxheight>768</maxheight>
    <maxonstage>120</maxonstage>
    <maxwitheffect>80</maxwitheffect>
  </performance>
  <server>
    <onhost>yes</onhost>
    <load>http://localhost:'''+ port + '''/mukiocache/mukioplayer_py/danmu.xml</load>
    <send></send>
    <gateway></gateway>
  </server>
</conf>
    '''
    xml_to_write = xml_to_write.encode("utf8")
    os.chdir(py_path)
    f = open('./conf.xml', "w")
    f.write(xml_to_write)
    f.close()
    video_filename_url = ''
    video_filename_url = urllib.quote(video_newfilename)
    webpage_to_write = '''<html>

<head>
<title>'''+ video_filename + '''- Mukioplayer-Py-Mac</title>
</head>

<body>
<embed id="MukioPlayer"
src="http://localhost:'''+port+'''/mukioplayerplus.swf?file=http://localhost:'''+port+'''/mukiocache/mukioplayer_py/'''+video_filename_url+'''&type=video&sort=new"
width="99%" height="99%" type="application/x-shockwave-flash" allowscriptaccess="always" quality="high" allowfullscreen="true" />
</body>

</html>
'''
    #webpage_to_write = webpage_to_write.replace('\\', '').encode("utf8")
    webpage = open('./webpage.htm', "w")
    webpage.write(webpage_to_write)
    webpage.close()
    Process(target=http_server, ).start()
    os.chdir(py_path)
    os.system('cp webpage.htm  '  + real_cache_dir)
    os.system('cp favicon.ico  ' + real_cache_dir)
    webbrowser.open('http://localhost:'+port+'/mukiocache/mukioplayer_py/webpage.htm')



v_relpath = raw_input('Vid')
#v_relpath = v_relpath.encode('utf-8')
X_relpath = raw_input('XML')
#X_relpath = X_relpath.encode('utf-8')

main(v_relpath, X_relpath)