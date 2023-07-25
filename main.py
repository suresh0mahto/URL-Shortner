
import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("700x350")
root.title("URL Shortner")
root.configure(bg="#2AA8F2")

urlmain = StringVar()
urlshortmain = StringVar()
def urlShortner():
    urladdress = urlmain.get()
    urlshort = pyshorteners.Shortener().tinyurl.short(urladdress)
    urlshortmain.set(urlshort)

def copyurl():
    urlshort = urlshortmain.get()
    pyperclip.copy(urlshort)

Label(root,text="URL Shortner",font=('Arial', 20)).pack(pady=20)
Entry(root,textvariable=urlmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Shorten URL",command=urlShortner).pack(pady=7)
Entry(root,textvariable=urlshortmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Copy Url",command=copyurl).pack(pady=5)

root.mainloop()
