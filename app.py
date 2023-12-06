import streamlit as st
import numpy as np
from PIL import Image
import cv2 



st.set_option('deprecation.showfileUploaderEncoding', False)




file = st.file_uploader("ouvrir une image", type=["jpg", "png"])


if file is not None:

	pillow_img = Image.open(file)
	img = np.asarray(pillow_img)
	st.image(img, caption="image originale")


	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	st.image(gray, caption="image noir et blanc")

		
	(thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	st.image(blackAndWhiteImage, caption="image a un seuil")



	kernel = np.ones((3,3), np.uint8)
	img_erosion = cv2.erode(blackAndWhiteImage, kernel, iterations=2)
	st.image(img_erosion, caption="erosion")


	img_dilation = cv2.dilate(img_erosion, kernel, iterations=2)
	st.image(img_dilation, caption="delatation")

	blur = cv2.blur(img_dilation, (5,5)) 
	st.image(blur, caption="image blur")



