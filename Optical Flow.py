#import librarys
import numpy as np
import cv2	

# params for ShiTomasi corner detection
st_params = dict( maxCorners = 30,
                       qualityLevel = 0.2,
                       minDistance = 2,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1))#accuracy or speed
#Video capture
cap = cv2.VideoCapture('Video/run.mp4')
#color for optical flow
color = (0, 255, 0) #RBG
#read the capture and get the first fram
ret, first_frame = cap.read()
#convert frame to Grayscale
prev_gray = cv2.cvtColor(first_frame,
						 cv2.COLOR_BGR2GRAY)
#find the strongest corners in the frst frame
prev = cv2.goodFeaturesToTrack(prev_gray,
								mask = None,
								**st_params)
#while
while(cap.isOpened() ) :
		
	#read the capture and get the first frame
	ret, fram = cap.read()
	#convert all frame to gray sclae (privously we did only the first frame)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#calculate the optical flow by lucas -kanade
	next, status, error = cv2.calcOpticalFlowPyrLK(prev_gray, prev, None, **lk_params)
	#select a good feature for the previous position
	good_old = prev[status==1]
	# Select good feature for the next position
    good_new = next[status==1]
    #draw optical flow track 
    for i,(new,old) in enumerate(zip(good_new,good_old)):
    	#return coordinate for the new point
    	a,b = new.ravel()
    	#return coordinate for the old point
    	c,d = old.ravel()
    	#draw line between new and old
    	mask = cv2.line(mask,
    					(a,b),
    					(c,d),
    					color,
    					 2)
    	#draw filed section
    	frame = cv2.Circle(frame,
    						(a, b),
    						3,		#diameter
    						color,
    						-1)
    	#overlay optical flow on orginal frame
    	output = cv2.add(fram, mask)
    	#update previous frame
    	prev_gray = gray.copy()
    	#update the preious good feature
    	prev = good_reshape (-1,1,2)
    	#open new window and display the output
    	cv2.imshow("optical Flow", output)
    	#close the frame
    	if cv2.waitKey(300) & 0xFF == "q": #300 milisecond
    		break
#Release and Distory
cap.release() 
cv2.destroyAllWindows()

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while(1):
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)