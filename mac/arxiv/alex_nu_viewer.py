#!/usr/bin/python 
import numpy as np

import sys

import matplotlib
import matplotlib.pyplot as plt

from ROOT import larcv
larcv.load_pyutil

import _init_paths
from fast_rcnn.config import cfg

entries = None

with open("/stage/vgenty/NuDevKit/train_1.txt") as f:
    entries = f.read()

entries = [im for im in entries.split("\n") if im != "" ] 

cfg.IMAGE_LOADER = "SinglepLoader"
cfg.ROOTFILES   = ["/stage/vgenty/train_nu.root"]

cfg.IMAGE2DPROD  = "train"

import lib.utils.root_handler as rh

for i,entry in enumerate(entries):
    entry = int(entry)    
    
    imm = rh.get_image(entry)
    
    annoz = None
    with open( "/stage/vgenty/NuDevKit/Annotations/{}.txt".format(entry)) as f:
        annoz = f.read()

    annos_v = annoz.split("\n")
    
    a_v = []
    for annoz in annos_v:
        if annoz == '': continue
        annoz = annoz.split(" ");
        annoz = annoz[1:]

        aa = []
        for anno in annoz:
            anno = anno.rstrip()
            aa.append(float(anno))
        a_v.append(aa)
    

    fig,ax = plt.subplots(figsize = (12,12))
    imm = imm.astype(np.uint8)
    im = np.zeros([imm.shape[0],imm.shape[1]] + [3])
    for i in xrange(3):
        im[:,:,i] = imm[:,:,0]

    plt.imshow(im[:,:,(2,1,0)])

    plt.axis('off')
    for b in a_v:
        ax.add_patch(plt.Rectangle( (b[0],b[1]),
                                    b[2]-b[0], 
                                    b[3]-b[1],
                                    fill=False,edgecolor='red',linewidth=2.5) )


    ax.set_title("ENTRY: {}".format(entry))
    plt.savefig("f_entry_{}.png".format(entry))
    print "entry: {}".format(entry)
    # print "that's fine: {}".format(a)

    if i == 25:
        break
