import cv2                                                      #for getting all the pixel that belong to our input

cap=cv2.VideoCapture(0)                             #if you have zero webcam except one inbuilt then,VideoCapture(0),
                                                                        #if you have more than one webcam, you want to use different webcam except builtin
                                                                        #you can change 0 to 1 or 0 to 2, for detecting object


cap.set(cv2.CAP_PROP_FRAME_WIDTH,10000)                   #1080,from 0 to1000......,basically it is changing
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,10000)                  #the size of frame

while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)      #converting our input image from the original BGR color
                                                                                                    #space into HSV image

    height,width,_=frame.shape

    cx=int(width/2)                                                         #in opencv, pixel must be integer format
    cy=int(height/2)


    pixel_center=hsv_frame[cy,cx]                                  #print pixel value
                                                                                        #frame will print the value in BGR
                                                                                        #hsv_frame will print the value in HSV 

    hue_value=pixel_center[0]                                   #Taking the hue value only for color detection


    color="Undefined"
    if hue_value<5:
        color="RED"

    elif hue_value<22:
        color="ORANGE"

    elif hue_value<33:
        color="YELLOW"

    elif hue_value<78:
        color="GREEN"

    elif hue_value<84:
        color="LIGHT GREEN"

    elif hue_value<100:
        color="SKY BLUE"
        
    elif hue_value<131:
        color="BLUE"

    elif hue_value<156:
        color="VIOLET"

    elif hue_value<167:
        color="PINK"
        
    else:
        color="RED"
    
    #print(pixel_center)                                                            #if you will print(pixel_center) value then your system will slow down
                                                                                                 #you want to press CTRL+c or CTRL+q for existing.
                                                                                                #sometimes, it shows python isn't responding
    pixel_center_bgr=frame[cy,cx]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])


   
    cv2.putText(frame,color,(10,50),3,1,(b,g,r),2)                  #(img,text,org,(fontface),fontscale,color,thickness)
                                                                                                #we can change fontface,fontscale,color and thick. also
    
    cv2.circle(frame,(cx,cy), 5, (25,0,0), 3)                               #(img,(center),radius,(color),thickness)
    
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(10)                                                     #cv2.waitKey(0) or cv2.waitKey() will click current photo,when we will try to close frame(camera tab)
                                                                                          #it will click again your current photo

                                                                                         #cv2.waitKey(1) or cv2.waitKey(anynumber) will open camera

    if key==27:                                                                 #ctrl+Q will close all windows
        break

cap.release()
cv2.destroyAllWindows()
