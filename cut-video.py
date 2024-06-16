from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    h, m, s = map(int, time_str.split(':'))
    # Convert to seconds
    return h * 3600 + m * 60 + s

def cut_video(input_video_path, start_time_str, end_time_str, output_video_path):
    # Convert start and end times to seconds
    start_time = convert_to_seconds(start_time_str)
    end_time = convert_to_seconds(end_time_str)
    # Cut the video
    with VideoFileClip(input_video_path) as video:
        new = video.subclip(start_time, end_time)
        new.write_videofile(output_video_path, audio_codec='aac')

# Replace 'your_video.mp4' with the path to your video file
# Replace 'output.mp4' with the path to the output file
# Replace 'start_time' and 'end_time' with the start and end times of the part you want to cut (in hh:mm:ss format)
cut_video('videos/pepe argento en la peluquería.mp4', '00:01:00', '00:01:20', 'edits/result.mp4')