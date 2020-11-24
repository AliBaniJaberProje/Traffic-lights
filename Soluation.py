import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("img4-l4.png" , 1)
#resized1 = cv2.resize(img, (400 , 600), interpolation = cv2.INTER_AREA)
#cv2.imshow('Signs' , resized1 )
cv2.waitKey(0)
cv2.destroyAllWindows()


gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
x = cv2.medianBlur(gray, 1)

ret , img2 = cv2.threshold(x , 200 , 255 ,1)
#resized = cv2.resize(img2, (400 , 600), interpolation = cv2.INTER_AREA)
edges = cv2.Canny(img2,100,200)
cv2.imshow("th",img2)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i =0
for c in contours:
	epsilon = 0 * cv2.arcLength(contours[i], True)
	approx = cv2.approxPolyDP(contours[i], epsilon, True)
	cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
	i = i+1

#cv2.drawContours(img, contours, -1, (0, 255,0), 2)
#cv2.findContours()

for i in contours:
	M = cv2.moments(i)
	if M["m00"] != 0:
		cx = int(M["m10"] / M["m00"])
		cy = int(M["m01"] / M["m00"])

	else:
		cx, cy = 0, 0
cv2.imshow('result' , img)
print(len(contours))
nuber_of_contours=len(contours)

if nuber_of_contours==42:
	print(" deagerous descent" )
if nuber_of_contours==28:
	print(" bumpy road")
if nuber_of_contours==7:
	print(" bumpy road")
if nuber_of_contours==6:
	print(" bumpy road")
if nuber_of_contours==115:
	print(" traffic ligts ahead ")
if nuber_of_contours==60:
	print(" traffic ligts ahead ")
if nuber_of_contours==65:
	print(" Stop ")
if nuber_of_contours==15:
	print(" Stop ")
if nuber_of_contours==82:
	print("no entry ")
if nuber_of_contours==17:
	print(" give way")
if nuber_of_contours==0:
	print("no parking")
if nuber_of_contours==19:
	print("no parking")
if nuber_of_contours==1:
	print("no parking")
if nuber_of_contours==82:
	print(" go straight ")
if  nuber_of_contours==77:
	print(" go right ")
if nuber_of_contours==40:
	print(" Exit  ")
if nuber_of_contours==35:
	print(" Freeway entry  ")
if nuber_of_contours==9:
	print("  Circle ")

if nuber_of_contours==102:
	print(" local destination ")
if nuber_of_contours==105:
	print(" tourist destination ")
if nuber_of_contours==135:
	print(" tourist destination ")
if nuber_of_contours==165:
	print(" major rood sign  ")
if nuber_of_contours==156:
	print(" major rood sign  ")
if nuber_of_contours==109:
	print(" end speed limt  ")







cv2.waitKey(0)
cv2.destroyAllWindows()