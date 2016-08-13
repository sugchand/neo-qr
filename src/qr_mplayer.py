#! /usr/bin/python
# -*- coding: utf8 -*-
# The QR media player to play video for specific QR code. 
#
__author__ = "Sugesh Chandran"
__copyright__ = "Copyright (C) The neoview team."
__license__ = "GNU Lesser General Public License"
__version__ = "1.0"

import qr_code_dic
import os
import sys

curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(curr_dir, 'lib')))
try:
    import os_lib
except ImportError:
    os_lib = None

class qr_mplayer():
    '''
    The media player class to play specific video based on the QR code.
    '''
    def __init__(self):
        self.os_lib = os_lib.os_lib()

    def video_play(self, video_src = None):
        if video_src is None:
            return
        self.os_lib.execute_cmd("cvlc", [video_src, "--play-and-exit"])

    def get_video_src_from_qr(self, qrcode):
        if not qr_code_dic.qr_video_dic.has_key(qrcode):
            print("\uERROR: Failed to find QR code %s" %repr(qrcode))
            return None
        return qr_code_dic.qr_video_dic.get(qrcode)
