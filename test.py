import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import numpy as np

from Pose_Tracker import Tracker

path_to_data = "data/derek_thicc/"
tracker = Tracker()
nframes = 201
for i in range(100,100+nframes):
	json_file = path_to_data+"derek_thicc_000000000"+str(i)+"_keypoints.json"
	tracker.add_frame(json_file)
tracker.remove_null_points()
Lheelpath = np.array(tracker.get_joint_path("LHeel"))
x,y = Lheelpath[:,0],Lheelpath[:,1]

plt.plot(x,y,'.-')
plt.savefig("lheelpath.pdf",dpi=150)
