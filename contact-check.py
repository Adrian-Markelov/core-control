import cv2 
import numpy as np 


from Pose_Tracker import Tracker
import numpy as np
import os


path_to_data = "data/kick_mom/kick_3/"

os.system("bash contact-check.sh {}".format(path_to_data))

tracker = Tracker()


json_file = path_to_data+"foot_3_keypoints.json"
tracker.add_frame(json_file)
path = tracker.get_joint_path("RHeel")
cord = path[0] # [x, y] cord

print("************************************")
print("FOOT TRACKER: {}".format(cord))
print("************************************")



# Load image 
image = cv2.imread(path_to_data+'../no_foot.jpg', 0)
#image = image[1100:3000,:]

scale_percent = 20 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
  
# Set our filtering parameters 
# Initialize parameter settiing using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params() 
  
# Set Circularity filtering parameters 
params.filterByCircularity = True 
params.minCircularity = 0.2
  
# Create a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params) 
      
# Detect blobs 
keypoints = detector.detect(image) 

print("************************************")
print(keypoints)
print("************************************")
  
# Draw blobs on our image as red circles 
blank = np.zeros((1, 1))  
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
  
number_of_blobs = len(keypoints) 
text = "Number of Circular Blobs: " + str(len(keypoints)) 
cv2.putText(blobs, text, (20, 550), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 
  
# Show blobs 
cv2.imshow("Filtering Circular Blobs Only", blobs) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 




