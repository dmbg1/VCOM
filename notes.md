# Notes Project

## Ideas

Separate blue and red signs by hue. Use bitwise operations to make everything black except the sings we wawnt

[Cheat for separating red and blue](https://medium.com/lifeandtech/traffic-sign-detection-recognition-f6e741543619)

Detect circles for rounded signs

Detect edges to separate STOP sings

HOG feature detecter

Make several clean datasets (make an iteration with only 1 sign per photo)


## Take into consideration

Dataset is not clean

[XML parser] (https://www.edureka.co/blog/python-xml-parser-tutorial/#modules) 


## Goals

Make a jupyter notebook

Separate in 3 classes:
- STOP signs
- Red circles
- Blue squares/rectangles

## Pipeline

- Import image
    - Remove unnecessary images for project
        - Traffic lights
    - Create list of objects with all necessary information
        - filename
        - sign type
        - size ?
    - Create validation list with solution
- Extract features
    - Apply smoothing
    - Detect sign and remove background
        - Possible through hue ? 
    - Point/Edge detection
    - Circle detection
- Classify picture
    - Make prediction
    - Add prediction to validation list
- Analysis of performance

## Types of signs in dataset

