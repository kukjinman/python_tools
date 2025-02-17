import cv2
from tqdm import tqdm

# OpenCV에서 제공하는 얼굴 검출기 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# 모자이크 효과를 적용하는 함수
def apply_mosaic(image, x, y, w, h, mosaic_scale=0.05):  # Adjusted mosaic_scale for more pixelation
    roi = image[y:y+h, x:x+w]
    roi = cv2.resize(roi, (int(w * mosaic_scale), int(h * mosaic_scale)), interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = roi
    return image

# 비디오 파일 열기
cap = cv2.VideoCapture('sample_vedio.mp4')

# 출력 비디오 저장을 위한 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

# 진행률 표시를 위한 총 프레임 수 가져오기
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 진행률 표시와 함께 비디오 모자이크 처리
with tqdm(total=total_frames, desc="Processing Video") as pbar:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 프레임을 그레이스케일로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 프레임에서 얼굴 검출
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(20, 20))

        # 검출된 얼굴에 모자이크 적용
        for (x, y, w, h) in faces:
            frame = apply_mosaic(frame, x, y, w, h)

        # 출력 비디오에 모자이크 된 프레임 쓰기
        out.write(frame)

        # 진행 된 frame 수 업데이트
        pbar.update(1)


# 비디오 캡처 및 작성기 객체 해제
cap.release()
out.release()
cv2.destroyAllWindows()