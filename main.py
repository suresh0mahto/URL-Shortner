
import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("700x350")
root.title("URL Shortner Application")
root.configure(bg="#000000")

urlmain = StringVar()
urlshortmain = StringVar()
def urlShortner():
    urladdress = urlmain.get()
    urlshort = pyshorteners.Shortener().tinyurl.short(urladdress)
    urlshortmain.set(urlshort)

def copyurl():
    urlshort = urlshortmain.get()
    pyperclip.copy(urlshort)


Label(root,text="URL Shortner App",font=('Arial', 12)).pack(pady=10)
Entry(root,textvariable=urlmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Generate Short Url",command=urlShortner).pack(pady=7)
Entry(root,textvariable=urlshortmain,width=50,font=('Arial 14')).pack(padx=10, pady=10)
Button(root,text="Copy Short Url",command=copyurl).pack(pady=5)

root.mainloop()