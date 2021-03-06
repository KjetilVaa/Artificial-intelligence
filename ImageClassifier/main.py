import os
import numpy as np
## Keras is a wrapper over tenserflow - easier to program with
from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras import optimizers

## Collect data

img_height, img_widht = 150, 150
training_data = load_data("/training")
validation_data = val_data("/validation")

## Build model 

model = Sequential()

# Rescale the pixel values
datagen = ImageDataGenerator(rescale=1./255)

# Retrieve images and their classes for train and validation
train_generator = datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=16,
        class_mode="binary")

validation_generator = datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode="binary")


## Build model
model = Sequential()
model.add(Convolution2D(32, 3, 3, input_shape=(img_width, img_height,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(32, 3, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(64, 3, 3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation("sigmoid")) ##Using sigmoid activiation function
model.compile(loss="binary_crossentropy", optimizer="rmsprop",metrics=["accuracy"])

## Training
nb_epoch = 30
nb_train_samples = 2048 ## Half dogs and half cats
nb_validation_samples = 832


model.fit_generator(
        train_generator,
        samples_per_epoch=nb_train_samples,
        nb_epoch=nb_epoch,
        validation_data=validation_generator,
        nb_val_samples=nb_validation_samples)

print(model.evaluate_generator(validation_generator, nb_validation_samples))


