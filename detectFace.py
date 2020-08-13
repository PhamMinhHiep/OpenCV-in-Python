import cv2 as cv


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv.cvtColor(frame, 	cv.COLOR_BGR2GRAY)

	face = face_cascade.detectMultiScale(frame)

	for x, y, w, h in face:
		cv.rectangle(frame, (x, y), (x+w, y+h), (255,0,255), 2)
		#roi_gray = frame[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_color)

		for x2, y1, w1, h1 in eyes:
			cv.rectangle(frame, (x+ x1, y+ y1), (x + x1 + w1, y + y1 + h1), (255,0,0), 2)
	cv.imshow('Face Detection', frame)

	if cv.waitKey(20) == ord('q'):
		break
cap.release()
cv.destroyAllWindow()
