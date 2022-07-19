import cv2
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def img_analyze(img_name):
	img = cv2.imread(img_name)
	#mode 0 R.G.B
	df = []
	#mode 1 H.S.V

	for i in range(2):
		dfx = [i for i in range(0,256)]
		dfy = [0 for i in range(0,256)]
		dfy2 = [0 for i in range(0,256)]
		dfy3 = [0 for i in range(0,256)]
		if i==1:
			img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		for i in range(3):
			for j in img[:,:,i]:
				for v in j:
					if i==0:
						dfy[v] = dfy[v]+1
					elif i==1:
						dfy2[v] = dfy2[v]+1
					else:
						dfy3[v] = dfy3[v]+1
		df.append([dfx,dfy,dfy2,dfy3])
	return df

def plot_img(df):
	fig = make_subplots(rows=3, cols=2)
	for i in range(1,3):
		for j in range(1,4):
			fig.append_trace(go.Scatter(
			x=df[i-1][0],
			y=df[i-1][j],
			), row=j, col=i)
	fig.update_layout(height=600, width=1200, title_text="B.G.R H.S.V")
	fig.show()

