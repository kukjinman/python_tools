import cv2
from tqdm import tqdm

# Load the pre-trained face detector from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



# Function to apply mosaic effect to a region of interest (ROI)
def apply_mosaic(image, x, y, w, h, mosaic_scale=0.05):  # Adjusted mosaic_scale for more pixelation
    roi = image[y:y+h, x:x+w]
    roi = cv2.resize(roi, (int(w * mosaic_scale), int(h * mosaic_scale)), interpolation=cv2.INTER_LINEAR)
    roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = roi
    return image

# Open the video file
cap = cv2.VideoCapture('sample_vedio.mp4')

# Get the video writer initialized to save the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

# Get the total number of frames for the progress bar
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Process the video with a progress bar
with tqdm(total=total_frames, desc="Processing Video") as pbar:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(20, 20))

        # Apply mosaic to each detected face
        for (x, y, w, h) in faces:
            frame = apply_mosaic(frame, x, y, w, h)

        # Write the frame to the output video
        out.write(frame)

        # Update the progress bar
        pbar.update(1)

        # Display the frame (optional)
        # cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()