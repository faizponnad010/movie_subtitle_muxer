from send2trash import send2trash
import argparse,os,glob


def is_dir(path):
    return os.path.isdir(path)
def delete_subtitles_and_movies(movies,subtitles):
    for movie,subtitle in zip(movies,subtitles) :
        send2trash(movie)
        send2trash(subtitle)
def merge_files_in_folder(moviesFolder,subtitlesFolder,movieExtension,postFix):
    movieFiles=glob.glob(moviesFolder+"\*."+movieExtension)
    subtitleFiles=glob.glob(subtitlesFolder+"\*.srt")
    for movie,subtitle in zip(movieFiles,subtitleFiles) :
        merge_subtitle(movie,subtitle,postFix)
    delete_subtitles_and_movies(movieFiles,subtitleFiles)

def init_terminal_parser():
    parser = argparse.ArgumentParser(description='Merge subtitle with movie!!')
    parser.add_argument("-i","--input",help="Movie Input to merge")
    parser.add_argument("-s","--subtitle",help="subtitle file to merge")
    parser.add_argument("-po","--postfix",help="prefix to add to the new file_name",default="hard-sub")
    parser.add_argument("-ext","--extenstion",help="File Extension to search in folder(just for folder usage)",default="mp4")
    return parser.parse_args()

def merge_subtitle(moviefile,subtitle,postFix):
    base_path=os.path.dirname(moviefile)
    fileName=os.path.splitext(os.path.basename(moviefile))[0]
    extension=moviefile.split(".")[-1]
    outputPath=os.path.join(base_path,fileName+"-"+postFix+"."+extension)
    # print("ffmpeg -i '{0}' -i '{1}' -c copy '{2}'".format(moviefile,subtitle,outputPath))
    os.system('ffmpeg -i "{0}" -i "{1}" -c copy "{2}"'.format(moviefile,subtitle,outputPath))