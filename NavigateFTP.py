#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 17:34:31 2019

@author: hxtruong
"""
from ftplib import FTP
ftp = FTP("ftp.pyclass.com")
ftp.login("student@pyclass.com", "student123")
ftp.nlst()
ftp.nlst("Data")
ftp.cwd("Data")
ftp.cwd("..")
ftp.close()