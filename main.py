from Download import Download;


def main():
    try:
        #catch the quality of the video or music
        quality = int(input('type the quality : '));

        #system that will add multiple urls or not 
        urls = ();

        Continue = True;

        while Continue:

            url = input('type the url: ');

            cn = input('do you want to continue add urls? [y/n]: ').upper();

            urls = urls + (url,);

            if(cn == 'Y'):
                Continue = True;
            else:   
                Continue = False;
        
        #catch the type
        type = input('type the type [mp4, mp3, webp]: ');

        print(Download(quality, urls, type));
    
    except TypeError:
        print(TypeError);
    return 0;

if __name__ == "__main__":
    main();