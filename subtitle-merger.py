# from moviepy.video.tools.subtitles import SubtitlesClip
# from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.video.VideoClip import TextClip
# import imageio
# generator = lambda txt: TextClip(txt, font='Georgia-Regular',fontsize=24, color='white')
# sub = SubtitlesClip(r"C:\Users\Coderguy\Downloads\joey--first-season_english-401242\Joey S01E08.srt", generator)
# myvideo = VideoFileClip(r"F:\Series\s1\Joey.[Nightsdl.Com]..S01E08.mkv")
# final = CompositeVideoClip([clip, subtitles])
# final.to_videofile(r"F:\Series\s1\final.mp4", fps=myvideo.fps)

#ffmpeg -i F:\Series\s1\Joey.[Nightsdl.Com]..S01E08.mkv -i C:\Users\Coderguy\Downloads\joey--first-season_english-401242\JoeyS01E08.srt -c copy   Joey-S01E082.mkv
from merge_functions import *
args=init_terminal_parser()

if is_dir(args.input) and is_dir(args.subtitle):
    merge_files_in_folder(args.input,args.subtitle,args.extenstion,args.postfix)

else:
    merge_subtitle(args.input,args.subtitle,args.output)

