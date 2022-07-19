import cv2
img = cv2.imread("S-220215-01-40X-(G)PanCK(R)CD45(B)DAPI-20220310-_Top Slide_D_p00_0_A01f03d0.JPG")

#mode 1 R.G.B
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=2)

dfx = [i for i in range(0,256)]
dfy = [0 for i in range(0,256)]
dfy2 = [0 for i in range(0,256)]

dfy3 = [0 for i in range(0,256)]
#print(img[:,:,0].shape)
for i in range(3):
	for j in img[:,:,i]:
		for v in j:
			if i==0:
				dfy[v] = dfy[v]+1
			elif i==1:
				dfy2[v] = dfy2[v]+1
			else:
				dfy3[v] = dfy3[v]+1
#fig = px.line(x = dfx,y = dfy)
#fig.show()

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy,
), row=1, col=1)

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy2,
), row=2, col=1)

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy3,
), row=3, col=1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
dfx = [i for i in range(0,256)]
dfy = [0 for i in range(0,256)]
dfy2 = [0 for i in range(0,256)]

dfy3 = [0 for i in range(0,256)]
#print(img[:,:,0].shape)
for i in range(3):
	for j in img[:,:,i]:
		for v in j:
			if i==0:
				dfy[v] = dfy[v]+1
			elif i==1:
				dfy2[v] = dfy2[v]+1
			else:
				dfy3[v] = dfy3[v]+1
#fig = px.line(x = dfx,y = dfy)
#fig.show()

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy,
), row=1, col=2)

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy2,
), row=2, col=2)

fig.append_trace(go.Scatter(
    x=dfx,
    y=dfy3,
), row=3, col=2)


fig.update_layout(height=600, width=1200, title_text="B.G.R H.S.V")
fig.show()
#mode 2 R.G.B
