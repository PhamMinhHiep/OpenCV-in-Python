import cv2

cap = cv2.VideoCapture(r'D:\Ảnh+ Others\Video_All\video1402\video1402.mp4')

while True:
	success, img = cap.read()
	cv2.imshow('img', img)
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break