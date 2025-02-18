import cv2
from tqdm import tqdm

class VideoMosaic:
    def __init__(self, video_path, output_path='output_video.avi'):
        self.video_path = video_path
        self.output_path = output_path
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(video_path)
        self.fourcc = cv2.VideoWriter_fourcc('XVID')
        self.out = cv2.VideoWriter(output_path, self.fourcc, self.cap.get(cv2.CAP_PROP_FPS),
                                   (int(self.cap.get(3)), int(self.cap.get(4))))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def apply_mosaic(self, image, x, y, w, h):
        roi = image[y:y+h, x:x+w]
        roi = cv2.resize(roi, (int(w//20), int(h//20)), interpolation=cv2.INTER_LINEAR)
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = roi
        return image

    def close_video(self):
        self.cap.release()
        self.out.release()
        cv2.destroyAllWindows()

    def make_mosaic_video(self):
        with tqdm(total=self.total_frames, desc="Processing Video") as pbar:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(20, 20))

                for (x, y, w, h) in faces:
                    frame = self.apply_mosaic(frame, x, y, w, h)

                self.out.write(frame)
                pbar.update(1)

        self.close_video()