  
# File: strip_detector_test.py
# Author: @MichaelHannalla
# Project: Trurapid COVID-19 Strips Detection Server with Python
# Description: Python file for testing the strip detector based on detecto on a single input image

from detecto.core import Model
from detecto.utils import read_image
from detecto.visualize import plot_prediction_grid
import os

def main():

    model = Model.load('models/detector_weights.pth', ['medicament', 'vignette'])
    
    path = "data/eval"
    image_files = os.listdir(path)
    images = []
    start_idx = 14
    end_idx = 17
    
    for idx, image_file in enumerate(image_files):
        
        if idx < start_idx:
            continue

        full_path = path + "/{}".format(image_file)
        if full_path.endswith(".jpg"):
            test_image = read_image(full_path)
            images.append(test_image)

        
        if idx == end_idx:
            break
    
    # labels, boxes, scores = model.predict(test_image)
    
    plot_prediction_grid(model, images, dim=None, figsize=None, score_filter=0.6)
    
if __name__ == "__main__":
    main()
    