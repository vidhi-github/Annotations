#import all libraries
import cv2
from mtcnn import MTCNN

image_path="faces.jpeg"
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
detector=MTCNN()
faces=detector.detect_faces(image_rgb)
print("detected faces:",faces)
# 5 coordinates(box,keypoints,landmarks: nose,left mouth,right muth,left eye,right eye)

# bounding box(top,left,width ,height--x,y,w,h)
for face in faces:
    x,y,w,h=face['box']
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
output_path="output.jpg"
cv2.imwrite(output_path,image)
print("output is saved successfully")
