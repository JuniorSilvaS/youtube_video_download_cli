import tkinter as tk
from Download import Download;
class Interface:
    def start(self):
        root = tk.Tk()
        root.geometry("300x300")
        root.title("URL & Quality Input")

        # URL input
        tk.Label(root, text='Enter the URL:').pack(pady=5)
        url_entry = tk.Entry(root, width=30)
        url_entry.pack(pady=5)

        # Quality input
        tk.Label(root, text='Enter the quality:').pack(pady=5)
        quality_entry = tk.Entry(root, width=15)
        quality_entry.pack(pady=10)

        #
        tk.Label(root, text='Enter the type [mp4, mp3, webp]:').pack(pady=5)
        type_entry= tk.Entry(root, width=15)
        type_entry.pack(pady=10)
        

        # Button callback
        def aux():
            url = url_entry.get();
            quality = int(quality_entry.get());
            type = type_entry.get();
            
            print(Download(quality,(url), type));

        tk.Button(root, text="Submit", command=aux).pack(pady=5)
        root.mainloop()

# Run the app
interface = Interface()
interface.start()

# After the window closes, you can access:
# print(interface.url, interface.quality)
