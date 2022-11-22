#!/usr/bin/python3
import ftplib

with ftplib.FTP('145.192.1.20') as ftp:
    try:
        ftp.login('pzftp','pz123456')  
        wdir = ftp.pwd()
        print(wdir)

        ftp.cwd('/Telephoto/PHOTO')
        wdir2 = ftp.pwd()
        print(wdir2)
        files = []
        ftp.dir(files.append)
        print(files)
        
        files = ftp.nlst()
        print(files)

    except ftplib.all_errors as e:
        print('FTP error:', e) 