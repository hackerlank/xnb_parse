# coding=utf-8
"""
Dump info from XACT files
"""

import sys
import os
import time

from xnb_parse.xact.xwb import XWB


def read_xact(in_file, out_dir=None):
    in_file = os.path.normpath(in_file)
    print(in_file)
    xwb = XWB(filename=in_file)
    if out_dir is not None:
        xwb.export(out_dir)


def main():
    if 1 < len(sys.argv) <= 3:
        totaltime = time.time()
        in_file = sys.argv[1]
        out_dir = None
        if len(sys.argv) > 2:
            out_dir = sys.argv[2]
        read_xact(in_file, out_dir)
        print('> Done in {:.2f} seconds'.format(time.time() - totaltime))
    else:
        print('read_xact.py file.xwb export_dir')
