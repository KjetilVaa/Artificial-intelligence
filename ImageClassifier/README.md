# Image Classifier

This application classifies images as either dogs or cats based on 2048 pictures. It uses a CNN (Convoluional Neural Network) with sequential stack of layers (Keras allows each layer to be treated as object). Splits each image to pixels and pixel-intensity (RGB is each one layer each), and from there describe the probability of it being a certain class. 

## Data
Since the model is trained with about 2000 images, the dataset is pretty big and instead of uploading them on github you can download it here: https://www.kaggle.com/c/dogs-vs-cats/data

## Dependencies

- Keras
- Tenserflow
- numpy