import cv2 
import numpy as np 


from Pose_Tracker import Tracker
import numpy as np
import os


path_to_data = "data/alex/"

os.system("bash contact-check.sh {}".format(path_to_data))

tracker = Tracker()


json_file = path_to_data+"foot_3_keypoints.json"
tracker.add_frame(json_file)
path = tracker.get_joint_path("RHeel")
cord = path[0] # [x, y] cord

print("************************************")
print("FOOT TRACKER: {}".format(cord))
print("************************************")








