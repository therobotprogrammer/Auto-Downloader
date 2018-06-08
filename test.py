#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==========================================# 
# Author: Pranav
# If you find this code useful, 
# please include this section and give 
# credit to original author.  
#==========================================

import wget,sys,os

    dir_name = os.getcwd()
#project_dir = ('/home/deep_learning/')
common_utils_dir = project_dir + '/COMMON_UTILS'



data_to_download =  {    
    
    '/ORIGINAL_DATA/GLOVE':         [
                                        'titanic',
                                    ],


    '/ORIGINAL_DATA/TEXT':          [
                                        'http://alt.qcri.org/semeval2017/task1/data/uploads/sts2017.gs.zip',
                                        'http://alt.qcri.org/semeval2017/task1/data/uploads/sts2017.eval.v1.1.zip'
                                        
                                    ],
    
    '/COMMON_UTILS':  [
                                        'https://raw.githubusercontent.com/algorithmica-repository/deep-learning/master/2018-feb/common_utils/utils.py'
                                    ],
                    }


if os.path.isfile(project_dir + '/AutoDownloader.py'):
    os.remove(project_dir + '/AutoDownloader.py')
    
AutoDownloader_url = 'https://raw.githubusercontent.com/thegreatskywalker/my_deep_learning/master/AutoDownloader.py'
wget.download(AutoDownloader_url, out = 'AutoDownloader.py')

sys.path.insert(0, project_dir) 


from AutoDownloader import AutoDownloader
auto_dl = AutoDownloader()
auto_dl.initiate(project_dir, data_to_download)

auto_dl.showDirectory(project_dir,True, 2)

user_key = ""
token =""
auto_dl.setup_pushover_credintials(user_key,token)
auto_dl.send_notification('Test 4')




