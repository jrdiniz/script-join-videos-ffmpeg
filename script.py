import click
import ffmpeg
from moviepy.editor import *

@click.command()
@click.option('-o', '--opening', help='Opening Video')
@click.option('-m', '--middle', help='Middle Video')
@click.option('-c', '--closure', help='End Video')
def join_videos(opening, middle,closure):
    print(opening, middle, closure)

    opening_video = VideoFileClip(f"{opening}")
    opening_video.resize(height=1920)
    middle_video = VideoFileClip(f"{middle}")
    closure_video = VideoFileClip(f"{closure}")
    closure_video.resize(height=1920)
    
    final = concatenate_videoclips([opening_video, middle_video, closure_video],method='compose')
    
    final.resize(height=1920).write_videofile("new_video_v5.mp4")
    #final.to_videofile("new_video_v4.mp4")
    

if __name__ == '__main__':
    join_videos()
