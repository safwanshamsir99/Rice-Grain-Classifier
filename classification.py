from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import tensorflow as tf
from keras.models import model_from_json
import cv2
from matplotlib import pyplot as plt


IMG_SIZE = (224, 224)


def load_model():
    # load json and create model
    json_file = open('model/best_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model/best_model.h5")
    print("Loaded model from disk")
    return loaded_model


def get_image(pth, img_size=IMG_SIZE):
    img = load_img(pth, target_size=img_size)
    img = img_to_array(img) / 255.
    return img


def classify(pth):
    model = load_model()
    lbl = ['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']
    img = get_image(pth, img_size=IMG_SIZE)
    my_image = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    y_pr = model.predict(my_image)
    y_hat = np.argmax(y_pr, axis=1)
    yi_hat = lbl[y_hat[0]]
    yi_pr = y_pr[0].max()
    tit_sub = f"Prediction: {yi_hat} ({yi_pr:.1%})"
    print("\n")
    print(tit_sub)
    return tit_sub



def get_classificaton(ratio):
	ratio =round(ratio,1)
	toret=""
	if(ratio>=3):
		toret="Slender"
	elif(ratio>=2.1 and ratio<3):
		toret="Medium"
	elif(ratio>=1.1 and ratio<2.1):
		toret="Bold"
	elif(ratio<=1):
		toret="Round"
	toret="("+toret+")"
	return toret


def rice_quality_check(img):
    img = cv2.imread(img,0)
    ret,binary = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.float32)/9
    dst = cv2.filter2D(binary,-1,kernel)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    erosion = cv2.erode(dst,kernel2,iterations = 1)
    dilation = cv2.dilate(erosion,kernel2,iterations = 1)
    edges = cv2.Canny(dilation,100,200)

    contours,hierarchy = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print ("No. of rice grains=",len(contours))
    total_ar=0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        if(aspect_ratio<1):
            aspect_ratio=1/aspect_ratio
        print( round(aspect_ratio,2),get_classificaton(aspect_ratio))
        total_ar+=aspect_ratio
    avg_ar=total_ar/len(contours)
    print("Average Aspect Ratio=",round(avg_ar,2),get_classificaton(avg_ar))
    return f"Average Aspect Ratio = {round(avg_ar,2)} {get_classificaton(avg_ar)}"

