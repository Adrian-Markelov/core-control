#goal: convert 2d to 3d
import json

#user attributes
height = 5*12+10
wingspan = height

body_tracking = {"Nose":[],"Neck":[],"RShoulder":[],"RElbow":[],"RWrist":[],
"LShoulder":[],"LElbow":[],"LWrist":[],"MidHip":[],"RHip":[],"RKnee":[],"RAnkle":[],"LHip":[],"LKnee":[],"LAnkle":[],"REye":[],"LEye":[],"REar":[],"LEar":[],"LBigToe":[],"LSmallToe":[],"LHeel":[],"RBigToe":[],"RSmallToe":[],"RHeel":[],"Background":[]}
joints = body_tracking.keys()

#print(x['people'][0]['pose_keypoints_2d'])
#print(body_tracking.keys())

class Analysis():
	def __init__(self):
		self.body_tracking = {"Nose":[],"Neck":[],"RShoulder":[],"RElbow":[],
											"RWrist":[],"LShoulder":[],"LElbow":[],"LWrist":[],
											"MidHip":[],"RHip":[],"RKnee":[],"RAnkle":[],"LHip":[],
											"LKnee":[],"LAnkle":[],"REye":[],"LEye":[],"REar":[],
											"LEar":[],"LBigToe":[],"LSmallToe":[],"LHeel":[],
											"RBigToe":[],"RSmallToe":[],"RHeel":[],"Background":[]}
	def add_frame(self,json_fname):
		with open(json_fname,'r') as f:
			json_data = json.load(f)
  	pose_keypoints_2d_data = json_data['people'][0]['pose_keypoints_2d']
		for i in range(25):
			k = joints[i]
			x,y,score = pose_keypoints_2d_data[i*3:(i+1)*3]
			self.get_3d_coords([x,y])
			self.body_tracking[k].append([x,y,z])
	def get_3d_coords(pos2d):
		x,y = pos2d
		 v   

tracker = Tracker()
image_file = "data/derek_thicc/derek_thicc_000000000100_keypoints.json"
tracker.add_frame(image_file)
	
 
