import cv2

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=input('enter your id: ')
sampleNum=0
a=int(input('Enter Number of datasets to take:  '))

while(True):
    ret, img = cam.read()
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
     
        #incrementing sample number 
       sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
       cv2.imwrite("S/SS"+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w]) #
    cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
       break
    # break if the sample number is morethan 20
    elif sampleNum > a:
       
       break
   
cam.release()
cv2.destroyAllWindows()
