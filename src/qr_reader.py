#! /usr/bin/python
# -*- coding: utf8 -*-
# The QR reader module to decode QR codes.
#
__author__ = "Sugesh Chandran"
__copyright__ = "Copyright (C) The neoview team."
__license__ = "GNU Lesser General Public License"
__version__ = "1.0"

from qrtools import QR
import time
import cv2
import os
import re
import sys

curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(curr_dir, 'lib')))
try:
    import os_lib
except ImportError:
    os_lib = None

class qr_reader():
    '''
    class to match the QR image with
    specific information.
    '''
    def __init__(self):
        self.os_lib = os_lib.os_lib()

    def image_qr_read(self, filename):
        '''
        Read the QR image data from the image.
        '''
        qr_result = ""
        qr_data = QR(filename=filename)
        if qr_data.decode():
            print(qr_data.data)
            #print(qr_data.data_type)
            qr_result = qr_data.data_to_string().decode("utf-8-sig")
        return qr_result

    def webcam_qr_read(self):
        cv2.namedWindow("neoQR-preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        qr_result = ""
        while rval:
            cv2.imshow("neoQR-preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
            cache = self.os_lib.getImageName()
            cv2.imwrite(cache, frame)
            qr_result = self.image_qr_read(cache)
            time.sleep(0.1)
            self.os_lib.remove_file(cache)
            if qr_result:
                # Exit on valid QR code result
                break
        cv2.destroyWindow("neoQR-preview")
        # Bug in opencv, need to call waitkey with imshow to kill the window
        # completely. Otherwise the window get closed only when program exits.
        cv2.waitKey(-1)
        cv2.imshow("neoQR-preview", frame)
        self.os_lib.remove_file_matched_ext(curr_dir, 'jpg')
        return qr_result

if __name__ == "__main__":
    #qr_reader().image_qr_read("/home/sugesh/sree.jpg")
    qr_reader().webcam_qr_read()

