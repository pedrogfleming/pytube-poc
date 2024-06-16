from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    h, m, s = map(int, time_str.split(':'))
    # Convert to seconds
    return h * 3600 + m * 60 + s

def cut_video(input_video_path, time_ranges, output_video_path):
    with VideoFileClip(input_video_path) as video:
        for i, (start_time_str, end_time_str) in enumerate(time_ranges):
            # Convert start and end times to seconds
            start_time = convert_to_seconds(start_time_str)
            end_time = convert_to_seconds(end_time_str)
            # Cut the video
            new = video.subclip(start_time, end_time)
            # Save each part as a separate mp4 file
            new.write_videofile(f"{output_video_path}_{i}.mp4", audio_codec='aac')

# Replace 'your_video.mp4' with the path to your video file
# Replace 'output' with the base path to the output files
# Replace 'time_ranges' with a list of start and end times of the parts you want to cut (in hh:mm:ss format)
cut_video('videos/pepe argento en la peluquería.mp4', [('00:00:01', '00:00:10'), ('00:00:10', '00:00:20')], 'edits/output')
