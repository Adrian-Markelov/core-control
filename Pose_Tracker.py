#track body keypoints in 2d
import json

class Tracker():
	def __init__(self):
		self.body_tracking = {"Nose":[],"Neck":[],"RShoulder":[],"RElbow":[],
											"RWrist":[],"LShoulder":[],"LElbow":[],"LWrist":[],
											"MidHip":[],"RHip":[],"RKnee":[],"RAnkle":[],"LHip":[],
											"LKnee":[],"LAnkle":[],"REye":[],"LEye":[],"REar":[],
											"LEar":[],"LBigToe":[],"LSmallToe":[],"LHeel":[],
											"RBigToe":[],"RSmallToe":[],"RHeel":[],"Background":[]}
		self.joints = list(self.body_tracking.keys())
	def add_frame(self,json_fname):
		with open(json_fname,'r') as f:
			json_data = json.load(f)
		pose_keypoints_2d_data = json_data['people'][0]['pose_keypoints_2d']
		for i in range(25):
			k = self.joints[i]
			x,y,score = pose_keypoints_2d_data[i*3:(i+1)*3]
			#self.get_3d_coords([x,y])
			self.body_tracking[k].append([x,y])#,z])
	def remove_null_points(self):
		body_tracking_no_nulls = {}
		for k in self.joints:
			body_tracking_no_nulls[k] = []
			for pos2d in self.body_tracking[k]:
				if pos2d[0] != 0 and pos2d[1] != 0:
					#not null
					body_tracking_no_nulls[k].append(pos2d)
		self.body_tracking = body_tracking_no_nulls
	def get_joint_path(self,k):
		return self.body_tracking[k]
	def get_3d_coords(pos2d):
		#TODO: actually get 3d coords
		pass
	def __str__(self):
		print(self.body_tracking)
	
 
