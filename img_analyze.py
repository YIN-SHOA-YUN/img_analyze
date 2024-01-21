import cv2
import numpy as np
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def img_analyze(img_name):
	img = cv2.imread(img_name,1) #read image as BGR mode
	df = []
	for i in range(2):
		dfy = [0 for j in range(0,256)]	#(0)B  (1)H
		dfy2 = [0 for j in range(0,256)]#(0)G  (1)S
		dfy3 = [0 for j in range(0,256)]#(0)R  (1)V
		if i==1:
			img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		for c in range(3):
			for j in img[:,:,c]:
				for v in j:
					if c==0:
						dfy[v] = dfy[v]+1
					elif c==1:
						dfy2[v] = dfy2[v]+1
					else:
						dfy3[v] = dfy3[v]+1
		df.append([dfy,dfy2,dfy3])
	return df

def plot_img(df):
	fig = make_subplots(rows=3, cols=2)
	for i in range(1,3):
		for j in range(1,4):	
			fig.append_trace(go.Scatter(
			x=df[i-1][0],	#0->BGR 1->HSV
			y=df[i-1][j],
			), row=j, col=i)#subplot position 
	fig.update_layout(height=600, width=1200, title_text="B.G.R H.S.V")
	fig.show()

path = input("Input the target path:")
target_type = input("target type(ex:jpg,bmp et al.):")

if __name__=='__main__':
	df = None
	check = 0
	for img_path in os.listdir(path):
		#Check target type
		if img_path.endswith(target_type):
			print(f"\rCurrent case:{check}",end='',flush=True)
			if check==0:
				df = np.array(img_analyze(os.path.join(path,img_path)))
				check = True
			else:
				df+=np.array(img_analyze(os.path.join(path,img_path)))
			check+=1
	new_df = []
	for i in range(len(df)):
		new_df.append(list(df[i]))
		new_df[i].insert(0,[i for i in range(0,256)])
	plot_img(new_df)
