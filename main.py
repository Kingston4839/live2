import os

os.system('ffmpeg -stream_loop -1 -re -i video.mp4 -stream_loop -1 -re -i http://stream.zeno.fm/cbqs837yss8uv -vcodec libx264 -pix_fmt yuvj420p -maxrate 2048k -preset ultrafast -r 12 -framerate 1 -g 50 -crf 51 -c:a aac -b:a 128k -ar 44100 -strict experimental -video_track_timescale 100 -b:v 500k -f flv  rtmp://a.rtmp.youtube.com/live2/1c2h-36kr-fu7h-vfvm-cftp')


