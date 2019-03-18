#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:39:23 2019

@author: Mxolisi
"""

import os
import csv
import subprocess
import cv2
 


class read_csv:
    
    file_name = ''
    file_path = ''
    read_lines = []
    train_data = ''
    dataset_path = ''
    files = ''
    
    def __init__(self, file_name, path, dataset_path,train_data):
        self.file_name = file_name
        self.file_path = path
        self.train_data = train_data
        self.dataset_path = dataset_path
        self.files = os.listdir(self.dataset_path)
        return
    
    #get frames
    def getFrame(self,sec,video_file,_file_name):
        video_file.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = video_file.read()
        if hasFrames:
            cv2.imwrite(_file_name+str(sec)+".jpg", image)     # save frame as JPG file
        return hasFrames
    
    #creating folders and sorting files
    
    def read_files(self):
        
        with open('../csv files/' + self.file_name, newline='') as csvFile:
            reader = csv.reader(csvFile, delimiter = ' ', quotechar='|') #reads all rows from the CSV file
            for row in reader: #Goes through all the rows on the data from the CSV      
                for file in self.files: #reads files from the training dataset
                    #print(file)
                    
                    #gets the file name
                    _file_name = file.split('.')[0]
                    
                    if row[0].split(',')[0].split('.')[0] == _file_name: #Compares the ID's from the dataset and CSV
                        folder_name = str(row[0].split(',')[1])
                        os.makedirs(self.train_data + '/' + folder_name, exist_ok=True) #creates folder according to the breed name
                        source = self.dataset_path + '/' +  file
                        video_file = cv2.VideoCapture(source)
                        destination = self.train_data + '/' + folder_name
                        os.chdir(destination)
                        frameRate = 5
                        sec = 0
                        
                        success = self.getFrame(sec,video_file,_file_name)
                        
                        count = 0
                        success = 1
                        while success:
                            sec = sec + frameRate
                            sec = round(sec, 2)
                            success = self.getFrame(sec,video_file,_file_name)
                            success, image = video_file.read()
                            cv2.imwrite(_file_name + "-%d.jpg" % count, image)
                            count += 1
                        
        return
        
    #Gets images from  a signle video into folders according to their classes
    
    def getImages(self, _indir, _outdir, _crop_dimension, _crop_size, _crop_rate):
        #os.path.join(os.getcwd(), 'convert.py')
        _commands = "../classes/convert.py --indir " + "'../dataset/Day_01'" + " --outdir '../dataset/train'" + " --crop " + _crop_dimension + " --size " + _crop_size + " --rate " + _crop_rate
        os.chdir('/Users/Mxolisi/Documents/Lab Work/Folders_from_CSV_Scripts/classes/')
        #convert.video2images(_indir, _outdir, _crop_dimension, _crop_size, _crop_rate)
        subprocess.call(["python", _commands], shell=True)
        
        return
    
#Main function

def main():
    
    _file_name = 'Combined_shoot4Classes.csv'
    _path = '../'
    _dataset_path = '/Users/Mxolisi/Documents/Lab Work/Folders_from_CSV_Scripts/dataset/Day_01'
    _train_data = '../train'
    
    _read_csv = read_csv(_file_name, _path, _dataset_path, _train_data)
    
    _read_csv.read_files()
    
if __name__ == "__main__":
    main()