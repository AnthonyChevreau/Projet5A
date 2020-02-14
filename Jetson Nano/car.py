#!/usr/bin/env python
# coding: utf-8


from keras.models import load_model
import numpy as np
import cv2
import h5py
import time
import snapshot
import comUART
from termcolor import colored
import crop 

model = load_model('my_model.h5')

def grayscale(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  return img

def equalize(img):
  img = cv2.equalizeHist(img)
  return img

def preprocessing(img):
  img = grayscale(img)
  img = equalize(img)
  #normalize the images, i.e. convert the pixel values to fit btwn 0 and 1
  img = img/255
  return img

	
try:
	while True:
		img = snapshot.takeAsnap()
		img = crop.cropimg()
		img = cv2.imread('he2.jpg')

		print('taken')
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		img = np.asarray(img)
		img = cv2.add(img,np.array([-10.0]))
		img = cv2.resize(img, (32, 32))
		img = preprocessing(img)
		img = img.reshape(1, 32, 32, 1)
		print("proc")


#Test image

		detectionstring = str(model.predict_classes(img))
		print("detected : "+detectionstring)

		classnbr = detectionstring[1:len(detectionstring)-1]

#classification
		if classnbr == "5":
			print(colored("limite 80km/h", 'green'))
			comUART.sendtoOpenMV("1")
			time.sleep(10)
		elif classnbr == "2":
			print(colored("limite 50km/h", 'green'))
			comUART.sendtoOpenMV("2")
			time.sleep(10)
		else:
			print(colored("dunno", 'red'))
			comUART.sendtoOpenMV("9")
			time.sleep(10)
		'''elif classnbr == "14":
			print("STOP")
			comUART.sendtoOpenMV("3")
			time.sleep(20)
		elif classnbr == "4":
			print(colored("limite 70km/h", 'red'))
			comUART.sendtoOpenMV("4")
			time.sleep(10)
		elif classnbr == "5":
			print(colored("limite 80km/h", 'red'))
			comUART.sendtoOpenMV("5")
			time.sleep(10)
		elif classnbr == "8":
			print(colored("limite 120km/h", 'red'))
			comUART.sendtoOpenMV("6")
			time.sleep(10)'''
		

except KeyboardInterrupt:
    print("Exiting Program")
