  
# File: strip_detector_test.py
# Author: @MichaelHannalla
# Project: Medicine Packages Sticker Detection
# Description: Main Python file for the project functionality

from detecto.core import Model
from detecto.utils import read_image
from detecto.visualize import plot_prediction_grid
import os
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    args = parser.parse_args()

    model = Model.load('models/detector_weights_v2.pth', ['medicament', 'vignette'])
    
    image_path = args.image_path 

    images = [read_image(image_path)]
    
    plot_prediction_grid(model, images, dim=None, figsize=None, score_filter=0.6)
    
if __name__ == "__main__":
    main()
    