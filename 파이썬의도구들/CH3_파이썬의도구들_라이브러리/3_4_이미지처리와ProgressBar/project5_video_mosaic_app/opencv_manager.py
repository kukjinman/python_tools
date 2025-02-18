import cv2
from tqdm import tqdm

def initialize_video_paths(input_path, output_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    return face_cascade, cap, out, total_frames


# 모자이크 효과를 적용하는 함수
def apply_mosaic(image, x, y, w, h):
    roi = image[y:y+h, x:x+w]
    roi = cv2.resize(roi, (int(w//20), int(h//20)), interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = roi

    return image

def close_video(cap, out):
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def make_mosaic_video(face_cascade, cap, out, total_frames):

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

