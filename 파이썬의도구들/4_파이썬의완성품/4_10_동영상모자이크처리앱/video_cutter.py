import cv2
from tqdm import tqdm

# Open the video file
cap = cv2.VideoCapture('input_video.mp4')
# Get the width and height of the video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Check if the video is 4K
if width == 3840 and height == 2160:
    print("The video is 4K resolution.")
else:
    print(f"The video resolution is {width}x{height}.")

# Get the video writer initialized to save the output video in mp4 format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('input_video_5sec.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate the total number of frames for 20 seconds
total_frames = int(fps * 5)

frame_count = 0

# Process the video with a progress bar
with tqdm(total=total_frames, desc="Cutting Video to 20 Seconds") as pbar:
    while cap.isOpened() and frame_count < total_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Write the frame to the output video
        out.write(frame)
        frame_count += 1

        # Update the progress bar
        pbar.update(1)

# Release the video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()