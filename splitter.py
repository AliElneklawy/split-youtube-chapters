from moviepy.video.io.VideoFileClip import VideoFileClip
import re



input_video_path = input('Path to the video: ')
timestamps_file = input('Path to the timestamps file: ')
names = []
timestamps = []
timestamps_scnds = []
pattern = r'(\d+:\d+:\d+)[^\w]*'
video_clip = VideoFileClip(input_video_path)


with open(timestamps_file, 'r') as f:
    for line in f:
        l = line.split(maxsplit=1)
        names.append(l[-1].removesuffix('\n'))
        timestamps.append(l[0])

max_len = len(timestamps[-1].split(':'))
if max_len == 2:
    for i in range(len(timestamps)):
        timestamps[i] = timestamps[i].strip()
        #timestamps[i] = '00:' * (max_len - len(timestamps[i].split(':'))) + timestamps[i]
        timestamps[i] = '00:' + timestamps[i]
else:
    for i in range(len(timestamps)):
        timestamps[i] = timestamps[i].strip()

for i in range(len(timestamps)):
    res = re.search(pattern, timestamps[i])
    ts = res.group(1)
    splitted = re.split(':', ts)
    hrs, mins, scnds = int(splitted[0]), int(splitted[1]), int(splitted[2])
    total_scnds = hrs * 60 * 60 + mins * 60 + scnds
    timestamps_scnds.append(total_scnds)

for i, start in enumerate(timestamps_scnds):
    if i < len(timestamps_scnds) - 1:
        end = timestamps_scnds[i + 1]
        output_path = f"{i+1}- {names[i]}.mp4"
        sub_clib = video_clip.subclip(start, end)
        sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

end = timestamps_scnds[-1]
output_path = f"{len(timestamps_scnds)}- {names[-1]}.mp4"
sub_clib = video_clip.subclip(timestamps_scnds[-1])
sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

video_clip.reader.close()
video_clip.audio.reader.close_proc()
