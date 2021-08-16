# File: dataset_check.py
# Author: @MichaelHannalla
# Project: Medicine Packages Sticker Detection
# Description: Python file for checking dataset doesn't have degen bboxes

import xml.etree.ElementTree as ET
import os

def main():
    data = "data/train"
    data_files = os.listdir(data)

    corrupt_counter = 0

    for data_file in data_files:
        if data_file.endswith(".xml"):
            current_xml_file_path = data + "/" + data_file

            # Passing the path of the
            # xml document to enable the
            # parsing process
            tree = ET.parse(current_xml_file_path)
            
            # getting the parent tag of
            # the xml document
            root = tree.getroot()
            
            object_one = root[6]

            bbox = object_one[4]
            xmin = int(bbox[0].text)
            ymin = int(bbox[1].text)
            xmax = int(bbox[2].text)
            ymax = int(bbox[3].text)
            if xmin > xmax or ymin > ymax:
                print("Corrupt bbox at file {}".format(current_xml_file_path))
                corrupt_counter += 1 

            try:
                object_two = root[7]
                bbox = object_two[4]
                xmin = int(bbox[0].text)
                ymin = int(bbox[1].text)
                xmax = int(bbox[2].text)
                ymax = int(bbox[3].text)
                if xmin > xmax or ymin > ymax:
                    print("Corrupt bbox at file {}".format(current_xml_file_path))
                    corrupt_counter += 1
            
            except IndexError:
                continue
            
            size = root[4]
            width = int(size[0].text)
            height = int(size[1].text)
            depth = int(size[2].text)

            if width == 0 or height == 0 or depth == 0:
                print("Corrupt bbox at file {}".format(current_xml_file_path))
                corrupt_counter += 1

            try:
                object_three = root[8]
                print("Found object three")

            except IndexError:
                continue

            
    
    print("Total number of corrupt files: {}".format(corrupt_counter))
            


            
if __name__ == "__main__":
    main()