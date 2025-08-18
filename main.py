import yt_dlp
#download_video function
def download_with_ytdlp(url, resolution="720"):
    ydl_opts = {
        #settings
        'format': f'bestvideo[height<={resolution}]+bestaudio/best/best',
        #place that will be download
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        #out put format
        'merge_output_format': 'mp4'
    };
    #download the video and show the information on the terminal
    ydl = yt_dlp.YoutubeDL(ydl_opts);
    info = ydl.extract_info(url, download=True);
    return ydl.prepare_filename(info);


video_url = input('type the video url : ');
resolution = int(input('type the resoltuion : '));

try:
    download_with_ytdlp(video_url, resolution);
except ValueError:
    print(ValueError);