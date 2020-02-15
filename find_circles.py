
#https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/


import cv2 
import numpy as np 
import copy





def main ():
  
	# Load image 
	image = cv2.imread('data/kick_mom/no_foot.jpg')
	print(type(image))

	image = downscaleImage(image, 20)


	#image = color_thres(image, 'hsv')

	image = blob_finder(image)

	## save 
	cv2.imshow("Filtering Circular Blobs Only", image) 
	cv2.waitKey(0) 
	cv2.destroyAllWindows() 
	#cv2.waitKey(0) 
	#cv2.destroyAllWindows() 

'''

  
# Show blobs 
cv2.imshow("Filtering Circular Blobs Only", blobs) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
'''



def blob_finder(image):
	# Set our filtering parameters 
	# Initialize parameter settiing using cv2.SimpleBlobDetector 
	params = cv2.SimpleBlobDetector_Params() 


	# Filter by Area.
	params.filterByArea = True
	params.minArea = 100

	# Set Circularity filtering parameters 
	params.filterByCircularity = True 
	params.minCircularity = 0.3

	# Filter by Inertia
	params.filterByInertia = True
	params.minInertiaRatio = 0.01
	params.maxInertiaRatio = 0.8

	# Create a detector with the parameters 
	detector = cv2.SimpleBlobDetector_create(params) 

	# Detect blobs 
	keypoints = detector.detect(image) 

	# Draw blobs on our image as red circles 
	blank = np.zeros((1, 1))  
	blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
								cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 


	#print(keypoints[0].pt)


	number_of_blobs = len(keypoints) 
	text = "Number of Circular Blobs: " + str(len(keypoints)) 
	cv2.putText(blobs, text, (20, 550), 
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 
	return blobs


def color_thres(image, mode):
	if mode == 'hsv':

		tol = 40

		bgr_green = np.uint8([[[0,255,0 ]]])
		hsv_green = cv2.cvtColor(bgr_green,cv2.COLOR_BGR2HSV)
		print(hsv_green)


		lower_bound = copy.deepcopy(hsv_green[0][0])
		lower_bound[0] = lower_bound[0]-tol
		lower_bound[1] = 100
		lower_bound[2] = 100

		upper_bound = copy.deepcopy(hsv_green[0][0])
		upper_bound[0] = upper_bound[0]+tol

		## convert to hsv
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

		print(lower_bound)
		print(upper_bound)

		## mask of green (36,25,25) ~ (86, 255,255)
		# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
		mask = cv2.inRange(hsv, lower_bound, upper_bound)
		#mask = cv2.inRange(hsv, ()), upper_bound)

		## slice the green
		imask = mask>0
		green = np.zeros_like(image, np.uint8)
		green[imask] = image[imask]

	else:
		# RGB
		mask = cv2.inRange(image, (0, 103, 0), (100, 255, 100))

		## slice the green
		imask = mask>0
		green = np.zeros_like(image, np.uint8)
		green[imask] = image[imask]

	return green


def downscaleImage(image, percent):
	scale_percent = 20 # percent of original size
	width = int(image.shape[1] * scale_percent / 100)
	height = int(image.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	return cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 




if __name__ == '__main__':
	main()


