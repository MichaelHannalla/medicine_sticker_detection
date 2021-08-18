
# medicine_sticker_detection

This repo is done as a project for detecting stickers (vignettes) on medicine packages
  
# Installation

1.  `git clone https://github.com/MichaelHannalla/medicine_sticker_detection.git` into any folder you like
2. Go to the folder by `cd medicine_sticker_detection`
3. Download and place the following model file [(Model File on Google Drive)](https://drive.google.com/file/d/1bI-AEuSCKJgLdqmdr5mi2AZG5rc-J170/view?usp=sharing) into the `models` directory.
4. Place your test images in the `test_images` folder. 
5. Install Python libraries using `pip install -r requirements.txt`

# Usage

`python detect_vignette.py test_images/<picture_name.jpg/png/jpeg>` 

This command will perform inference on the image given in that path.