from pytube import YouTube
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

def progress(stream, chunk, bytes_remaining):
    # Calculate the total file size in MB
    total_size_MB = stream.filesize / 1e6
    # Calculate the downloaded size in MB
    downloaded_MB = (stream.filesize - bytes_remaining) / 1e6
    # Calculate the remaining size in MB
    remaining_MB = bytes_remaining / 1e6
    # Calculate the percentage of the file that has been downloaded
    percentage = (100 * downloaded_MB) / total_size_MB
    # Clear the console output
    os.system('cls' if os.name == 'nt' else 'clear')
    # Print the percentage of download and the downloaded and remaining sizes
    print(f"Downloaded: {round(percentage)}% ({round(downloaded_MB)}MB of {round(total_size_MB)}MB, {round(remaining_MB)}MB remaining)")

def download_video(url):
    # Create YouTube object
    yt = YouTube(url, on_progress_callback=progress)

    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Download the video
    stream.download(output_path='./videos')
    
    print("Download complete!")
    path_to_video = './videos/' + yt.title + '.mp4'
    return path_to_video

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