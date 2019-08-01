#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:42:11 2019

@author: hxtruong
"""

from ftplib import FTP
import os

defaultDir = "/media/hxtruong/Data/Course/Data Processing with Python/DataProcessing"
def ftpDownloader(filename, host="ftp.pyclass.com", user="student@pyclass.com", password="student123"):
    ftp= FTP(host)
    ftp.login(user,password)
    ftp.cwd("Data")
    os.chdir(defaultDir)
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)
