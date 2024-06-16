import yt_utils

# Use the functions
path_to_video = yt_utils.download_video('https://www.youtube.com/watch?v=9vODNMKztoc')
print(path_to_video)
yt_utils.cut_video(path_to_video,  [('00:00:01', '00:00:10'), ('00:00:10', '00:00:20')], 'edits/output')