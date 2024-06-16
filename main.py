from pytube import YouTube
import os

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

    # Print when download is complete
    print("Download complete!")

# Replace 'your_url' with the URL of the YouTube video you want to download
download_video('https://www.youtube.com/watch?v=6djLgEFfn3M')
