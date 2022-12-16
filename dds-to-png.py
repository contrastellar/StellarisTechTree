from wand import image
import os.path
import argparse

parser = argparse.ArgumentParser(prog = 'dds-to-png', description='Program to convert all given files in a directory into png from dds, and output to a different directory.')
parser.add_argument('-i', 'input-dir')
parser.add_argument('-o', 'output-dir')

"""
with image.Image(filename="white_rect_dxt3.dds") as img:
    img.compression = "no"
    img.save(filename="white_rect_dxt3.png")
"""

"""
This is a script that takes a file folder that contains .dds 
files and then outputs them to a different file folder as .png's

"""
