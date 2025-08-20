import yt_dlp;
import os;

def Download(quality, urls, type):
    """
    download function

    Parameters:

    quality (int): the quality of the video of music that the user will download
    urls (turple) : the urls of the video that the user will download can be more than one url because it's a turple
    type (string) : the extension type like mp4 webp mp3

    Returns:

    str: return the download status 
    """

    #check if the user is in windows or linux
    
    if os.name == 'nt': #windows
        download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads');
    else: #linux
        download_folder = os.path.join(os.path.expanduser('~'), 'Downloads');
    
    
    #set the ydl_opts by the type extension selected
    ydl_opts = {};
    match type:
        case 'webp': # if its webp
            ydl_opts = {
                'formal' : f'bestvideo[height={quality}]+bestaudio/best[height={quality}]', 
                'outtmpl' : os.path.join(download_folder, '%(title)s.%(ext)s')
            };
        
        case 'mp4': # if this mp4
            ydl_opts = {
                'format': f'bestvideo[height={quality}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                'outtmpl' : os.path.join(download_folder, '%(title)s.%(ext)s'),
            };
        
        case 'mp3': # if its mp3
            ydl_opts = {
               'format': 'bestaudio/best',  # best available audio
                'outtmpl' : os.path.join(download_folder, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',     # convert to mp3
                    'preferredquality': f'{quality}',   # kbps
                }],
            };
    
    try:
        #set the options before the download
        ydl = yt_dlp.YoutubeDL(ydl_opts);
        #download the videos
        info = ydl.download(urls);
        return info;

    except TypeError:
        print(TypeError);
