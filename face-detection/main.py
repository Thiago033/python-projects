import cv2

trained_face_data = cv2.CascadeClassifier('face-detection/haarcascade_frontalface_default.xml')


# Image detector
# face_image = cv2.imread('IMAGE_PATH')
    
# grayscaled_face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

# face_coordinates = trained_face_data.detectMultiScale(grayscaled_face_image)

# (x, y, w, h) = face_coordinates[0]

# cv2.rectangle(face_image, (x, y), (x+w, y+h), (0,255,0), 2)

# cv2.imshow('Face Detector', face_image)
# cv2.waitKey()


# Video detector

# Webcam
# webcam = cv2.VideoCapture(0)

# video
faces_video = cv2.VideoCapture('VIDEO_PATH')

while True:
    successful_frame_read, frame = faces_video.read()
    
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow('Face Detector', frame)
    
    key = cv2.waitKey(1)
    
    if key==81 or key==113:
        break
