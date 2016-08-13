#! /usr/bin/python
# -*- coding: utf8 -*-
# The operating system interaction library to talk with os internals. 
#
__author__ = "Sugesh Chandran"
__copyright__ = "Copyright (C) The neoview team."
__license__ = "GNU Lesser General Public License"
__version__ = "1.0"

import time
import os
import platform
import subprocess

class os_lib():
    '''
    Library class for OS functions.
    '''
    def init(self):
        if platform.system() != 'Linux':
            print("os lib supports only on Linux")

    def getImageName(self):
        '''
        Get a unique image name based on time stamp
        '''
        localtime = time.localtime()
        capturetime = time.strftime("%Y%m%d%H%M%S", localtime)
        return capturetime + ".jpg"

    def remove_file(self, file_name):
        os.remove(file_name)

    def remove_file_matched_ext(self,dir_path, ext):
        ''''
        Function to remove all the files that matching a extension
        '''
        if not dir_path:
            return
        if not dir_path.endswith('/'):
            dir_path = dir_path + '/'
        
        filelist = [ f for f in os.listdir(dir_path) if f.endswith("." + ext) ]
        for f in filelist:
            f = dir_path + f
            os.remove(f)

    def execute_cmd(self, cmd, args):
        exec_cmd = []
        exec_cmd.append(cmd)

        if(len(args)):
            exec_cmd = exec_cmd + list(args)

        print("Excuting cmd: %s" %exec_cmd)
        try:
            out = subprocess.Popen(exec_cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        except Exception as e:
            print("Failed to run the bash command, " + e)
            raise e
        else:
            result, err = out.communicate()
            return result,err