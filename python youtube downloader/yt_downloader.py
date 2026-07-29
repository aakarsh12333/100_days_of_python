# ============================================================================
#   Importing Libraries ⇒ pytube and tkinter
# ============================================================================

import re
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
# ==============================================================================
# Create Display Window 
# ==============================================================================

root = Tk()  # ---------- used to initialize tkinter to create display window ----------
root.geometry('500x500') # ---------- used to set the window's width and height ----------
root.resizable(0, 0) # ---------- set the fix size of window ----------
root.title("DataFlair - Youtube video downloader") # ---------- used to give the title of window ----------

# =======================================================================================
# A text no one can change only it is shown for detailing like what the project does 
# =======================================================================================

Label(root, text= 'Youtube Video Downloader', font= 'arial 20 bold').pack()

'''
---------------------------------------------------------------------------
|
| Label() ⇒ Widget use to display text that user's can't able to modify.   |
| 
| root ⇒ is the name of the window                                         |
|
| text ⇒ which we display the title of the label                           |
|
| font ⇒ in which our text is written                                      |
|
| pack => organized widget in block                                         |
|
----------------------------------------------------------------------------
'''

# ======================================================================================================
# Create Field to Enter Link ⇒ In this we create an window to enter the link u have taken from youtube 
# ======================================================================================================

link = StringVar()

Label(root, text= 'Paste Link Here:', font= 'arial 15 bold').place(x= 160, y = 60)

link_enter = Entry(root, width= 70, textvariable=link).place(x = 32, y = 90)

'''
• link is a string type variable that stores the youtube video link that the user enters.
• Entry() widget is used when we want to create an input text field.
• width sets the width of entry widget
• textvariable used to retrieve the value of current text variable to the entry widget
• place() use to place the widget at a specific position
'''

# ==========================================================
# Create Fuction to Start Downloading ⇒ here logic start's 
# ==========================================================

def normalize_youtube_url(url):
    url = url.strip()
    if not url:
        return None

    short_match = re.search(r'(?:https?://)?(?:www\.)?youtu\.be/([^?&/]+)', url)
    watch_match = re.search(r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([^?&/]+)', url)
    embed_match = re.search(r'(?:https?://)?(?:www\.)?youtube\.com/embed/([^?&/]+)', url)

    if short_match:
        return f'https://www.youtube.com/watch?v={short_match.group(1)}'
    if watch_match:
        return f'https://www.youtube.com/watch?v={watch_match.group(1)}'
    if embed_match:
        return f'https://www.youtube.com/watch?v={embed_match.group(1)}'

    return url


def Downloader():     
    video_url = normalize_youtube_url(link.get())
    if not video_url:
        messagebox.showerror('Error', 'Please paste a YouTube link before downloading.')
        return

    if not re.match(r'https?://(www\.)?youtube\.com/watch\?v=[^?&]+', video_url):
        messagebox.showerror('Error', 'Please enter a valid YouTube video URL.')
        return

    try:
        url = YouTube(video_url)
        video = url.streams.first()
        video.download()
        Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)
    except Exception as exc:
        messagebox.showerror('Download failed', f'Could not download video:\n{exc}')

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()

'''
⇒ Url variable gets the youtube link from the link variable by get() function and then str() will convert the link in string datatype.

⇒ The video is download in the first present stream of that video by stream.first() method.

⇒ Button() widget used to display button on the window.

        • text which we display on the label
        • font in which the text is written
        • bg sets the background color
        • command is used to call the function
root.mainloop() is a method that executes when we want to run the program.
'''
