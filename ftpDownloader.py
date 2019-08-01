#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:42:11 2019

@author: hxtruong
"""

from ftplib import FTP

def ftpDownloader(host, user, password):
    ftp= FTP(host)
    ftp.login(user,password)
    print(ftp.nlst())