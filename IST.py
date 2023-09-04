from tkinter import *

root = Tk()
root.config(bg='#0a0703')
root.overrideredirect(True)

w = 382
h = 210

# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# calculate x and y coordinates for the Tk root window
x = ws-ws//4
y = hs-hs//3.3

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    

# Download Speed
def Download():
    show=''
    try:
        import speedtest
        st=speedtest.Speedtest(secure=True)
        show=str(st.download()//(1024**2))+' MbPS'
    except:
        show='No Internet Connection'
    Show=Label(text=show,font=('Arial',20,'bold'),fg='#90EE90',
                bg='#0a0703')
    Show.place(relx=0.5,rely=0.35,anchor=CENTER)

DownloadLabel=Label(text='Download Speed', 
                font=('Arial',18,'bold'),fg='white',
                bg='#0a0703'
                )
DownloadLabel.place(relx=0.3,rely=0.05)

DownloadButton=Button(text='Check',
                  font=('Arial',11,'bold'),fg='white',
                  bg='dark red',
                  command=Download)
DownloadButton.place(relx=0.13,rely=0.053)


# Upload Speed
def Upload():
    show=''
    try:
        import speedtest
        st=speedtest.Speedtest(secure=True)
        show=str(st.upload()//(1024**2))+' MbPS'
    except:
        show='No Internet Connection'
    Show=Label(text=show,font=('Arial',20,'bold'),fg='#90EE90',
                bg='#0a0703')
    Show.place(relx=0.5,rely=0.85,anchor=CENTER)

UploadLabel=Label(text='Upload Speed',
                font=('Arial',18,'bold'),fg='white',
                bg='#0a0703'
                )
UploadLabel.place(relx=0.35,rely=0.55)

UploadButton=Button(text='Check',
                  font=('Arial',11,'bold'),fg='white',
                  bg='dark red',
                  command=Upload)
UploadButton.place(relx=0.18,rely=0.54)






root.mainloop() # starts the mainloop
