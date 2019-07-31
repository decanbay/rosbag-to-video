#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: deniz
Istanbul Technical University
Deniz Ekin Canbay
canbay@itu.edu.tr
decanbay@gmail.com
"""

from __future__ import print_function
import rosbag
import numpy as np
import cv2
import os
import argparse
from time import time

def tourist():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
	    if file.endswith(".bag"):
                f_name=os.path.join(root, file)
	        print(f_name)
	        bag2video(file,root)	


def bag2video(bag_name,root_dir):
    bag = rosbag.Bag(os.path.join(root_dir, bag_name))
    for i in range(len(args.topics)):
        tt=[t.to_sec() for topic, msg, t in bag.read_messages(topics=args.topics[i])]
        fps=len(tt)/(tt[-1]-tt[0])
	res=cv2.imdecode( np.fromstring(msg.data, np.uint8),1).shape[1::-1]
	if len(args.outnames)>0:
            out = cv2.VideoWriter(os.path.join(root_dir,bag_name.split('.')[0]+"_"+str(args.outnames[i])+".avi"),cv2.VideoWriter_fourcc(*'h264'), fps,res)
        else:
            out = cv2.VideoWriter(os.path.join(root_dir,bag_name.split('.')[0]+"_"+str(i)+".avi"),cv2.VideoWriter_fourcc(*'h264'), fps,res)
	[out.write(cv2.imdecode( np.fromstring(msg.data, np.uint8),1)) for topic, msg, t in bag.read_messages(topics=args.topics[i])]
	out.release()

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description='Automatically Detect Bag Files and Extract Compressed Images as a Video in the Folder and Subfolders')
    parser.add_argument('--topics',default=["/decklink1/camera/image_compressed/compressed","/decklink2/camera/image_compressed/compressed"],help='Camera Topics',action='append')
    parser.add_argument('--outnames',default=["L","R"],help='File name additional for each topics',action='append')   
    args = parser.parse_args()
    if len(args.topics)>2:
	args.topics=args.topics[2::]
    else:
        pass
    if len(args.outnames)>2:
	args.outnames=args.outnames[2::]
    else:
        pass
    if len(args.topics) != len(args.outnames):
	print("Number of outnames != number of topics")	
	raise Exception()
    print(len(args.topics))
    print(args.topics)
    start=time()
    tourist()
    end=time()
    print("Total time="+str(end-start))
