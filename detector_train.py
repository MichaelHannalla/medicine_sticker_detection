# File: detector_train.py
# Author: @MichaelHannalla
# Project: Medicine Packages Sticker Detection
# Description: Python file for training the detector based on detecto on a single input image

from detecto.core import Dataset, Model

def main():

    train_dataset = Dataset('data/train')
    model = Model(['medicament', 'vignette'])
    val_dataset = Dataset('data/eval')
    losses = model.fit(train_dataset, val_dataset, epochs=10, learning_rate=0.01,
                   gamma=0.2, lr_step_size=5, verbose=True)

    
    model.save('models/detector_weights.pth')

if __name__ == "__main__":
    main()