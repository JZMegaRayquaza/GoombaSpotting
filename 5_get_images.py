import cv2 
import os 

video = cv2.VideoCapture('Goomba_Spotting.mp4') 


# Create a folder named data 
if not os.path.exists('data'): 
	os.makedirs('data')

i = 0

while i < 1000:
	ret, frame = video.read() 

	if not ret:
		break

	# Only get every 60th frame for annotating (after loading)
	if i > 200 and i % 60 == 0:
		name = './data/frame' + str(i) + '.jpg'
		print ('Creating...' + name) 

		cv2.imwrite(name, frame) 
	i += 1

video.release() 
cv2.destroyAllWindows() 
