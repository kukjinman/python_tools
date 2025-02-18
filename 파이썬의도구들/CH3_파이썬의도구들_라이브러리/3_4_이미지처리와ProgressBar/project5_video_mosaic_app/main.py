# non 클래스 버전
from opencv_manager import initialize_video_paths, make_mosaic_video, close_video

face_cascade, cap, out, total_frame = initialize_video_paths('sample_video.mp4', 'output_video.avi')
make_mosaic_video(face_cascade, cap, out, total_frame)
close_video(cap, out)



# # 클래스 버전
# from opencv_manager_classversion import VideoMosaic
#
# video_path = 'sample_video.mp4'
# output_path = 'output_video.avi'
#
# video_mosaic = VideoMosaic(video_path, output_path)
# video_mosaic.make_mosaic_video()







