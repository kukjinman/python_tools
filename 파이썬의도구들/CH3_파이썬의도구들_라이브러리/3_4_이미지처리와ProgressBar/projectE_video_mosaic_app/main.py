from opencv_manager import VideoMosaic

video_path = 'sample_video.mp4'
output_path = 'output_video.avi'

#0 VideoMosaic 클래스 객체 생성
video_mosaic = VideoMosaic(video_path, output_path)

#2 make_mosaic_video 함수 호출
video_mosaic.make_mosaic_video()
