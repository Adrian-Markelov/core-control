import numpy as np

from Pose_Tracker import Tracker

path_to_data = "data/kick_mom/kick_3/"
tracker = Tracker()
#nframes = 1
#for i in range(100,100+nframes):
json_file = path_to_data+"foot_3_keypoints.json"
tracker.add_frame(json_file)
tracker.remove_null_points()

parts = tracker.joints
xs,ys = [],[]
for part in parts:
	if len(tracker.body_tracking[part]) > 0:
		partpath = np.array(tracker.get_joint_path(part))
		x,y = partpath[:,0][0],partpath[:,1][0]
		print(part+" at ("+str(x)+","+str(y)+")")
		xs.append(x)
		ys.append(y)

circles = [(149.3118438720703, 204.853515625), (132.5070343017578, 338.04034423828125), (66.14899444580078, 423.40338134765625), (97.79817962646484, 314.6578063964844), (73.7011947631836, 132.65480041503906), (99.7248764038086, 372.0309753417969)]

def getdist(p1,p2):
	return np.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

mindist = 1000000
tmp = ()
for part in parts:
	for circle in circles:
		partpath = tracker.get_joint_path(part)
		if len(partpath) == 0: continue
		dist = getdist(circle,partpath[0])
		if dist < mindist:
			mindist = dist
			tmp = (circle,part)
print(tmp,mindist)
print(tracker.get_joint_path(tmp[1])[0])

#plt.plot(x,y,'.-')
#plt.savefig("lheelpath.pdf",dpi=150)
