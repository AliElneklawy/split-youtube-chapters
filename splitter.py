from moviepy.video.io.VideoFileClip import VideoFileClip
import re
import os


#dirname = os.path.dirname(os.path.realpath(__file__))
#files = os.listdir(dirname)

#for file in files:
#     if file == 'splitter.py': continue
     
input_video_path = input('Path to the video file: ')
timestamps_file = input('Path to the timestamps file: ')
timestamps_scnds = []
video_clip = VideoFileClip(input_video_path)

#str_pattern = r'^\d:\d\d\s*[-_!-*\s]*\s*(.*?)\s*(?=\d:\d\d\s*[-_!-*\s]*|$)'
#ts_pattern = r'^(\d:\d\d)\s*[-_!-*\s]*\s*.*$'

#print(os.path.dirname(input_video_path))

with open(timestamps_file, 'r') as f:
    lines = f.readlines()

lines = ''.join(lines)

#pattern = r"(\d+:\d+(?::\d+)?)\s*[-~:|#@>_^$+=]\s*(.+)"

#pattern = r'(\d+:\d+(?::\d+)?)\s*[-~:|#@>_^$+=\s]*\s*(.+)'
#pattern = r'(\d+:\d+(?::\d+)?)\s*[-\s]+(.+)'
pattern = r'([\d:]+)[\s-]+(.+)'

matches = re.findall(pattern, lines)

timestamps, chapter_names = zip(*matches)

ts = list(timestamps)
chapter_names = list(chapter_names)

for i in range(len(chapter_names)):
    chapter_names[i] = re.sub(r'[^\w\s-]', ' ', chapter_names[i])
    chapter_names[i] = re.sub(r'\s+', ' ', chapter_names[i])



#print(ts)
#print()
#print(chapter_names)
#exit()
#max_len = len(ts[-1].split(':'))
for i in range(len(ts)):
        ts[i] = ts[i].strip()
        #ts[i] = '00:' * (max_len - len(ts[i].split(':'))) + ts[i]
        if len(ts[i].split(':')) == 2:
            ts[i] = '00:' + ts[i]

for i in range(len(ts)):
    splitted = ts[i].split(':')
    hrs, mins, scnds = int(splitted[0]), int(splitted[1]), int(splitted[2])
    total_scnds = hrs * 60 * 60 + mins * 60 + scnds
    timestamps_scnds.append(total_scnds)

#print(ts)
#print()
#print(timestamps_scnds)
#print()
#print(chapter_names)
#exit()

for i, start in enumerate(timestamps_scnds):
    if i < len(timestamps_scnds) - 1:
        end = timestamps_scnds[i + 1] 
        fname = f"{i+1}- {chapter_names[i]}.mp4"
        output_path = os.path.join(os.path.dirname(input_video_path), fname)
        sub_clib = video_clip.subclip(start, end)
        sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

end = timestamps_scnds[-1]
output_path = f"{len(timestamps_scnds)}- {chapter_names[-1]}.mp4"
sub_clib = video_clip.subclip(timestamps_scnds[-1])
sub_clib.write_videofile(output_path, audio_codec='aac', fps=60)

video_clip.reader.close()
video_clip.audio.reader.close_proc()
