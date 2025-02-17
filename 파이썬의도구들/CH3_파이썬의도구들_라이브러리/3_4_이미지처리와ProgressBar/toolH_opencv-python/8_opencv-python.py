import cv2

#1 frontalface 정면 얼굴 인식용 필터
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#2 이미지 읽기
image = cv2.imread('man_iamge.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#3 얼굴 검출
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#4 모자이크 처리
for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
    face_region = cv2.resize(face_region, (w//10, h//10))
    face_region = cv2.resize(face_region, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = face_region

#5 결과 이미지 저장
cv2.imwrite('mosaic_image.jpg', image)