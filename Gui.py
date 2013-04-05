from tkinter import *
x='500'
y='150'
app = Tk()
app.title('Alfreds world')
app.geometry("800x500+100+25")
canvas = Canvas(app, height=500,width=800)
character = PhotoImage(file = "C:\Python Code 2012\Alfred's World\smiley.gif")
canvas.create_image(x, y, anchor=NE, image=character)
canvas.pack()
try:
   # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def key(event):
    if event.keysym == 'Escape':
        root.destroy()
        app.destroy()
    if event.char == event.keysym:
     # normal number and letter characters
        print( 'Normal Key %r' % event.char )
        if event.keysym == 'w':
            canvas.move('character',x , y + '50')
        elif event.char == 'Escape':
            root.destroy()
            app.destroy()
    elif len(event.char) == 1:
      # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
      # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )


root = tk.Tk()
print( "Press a key (Escape key to exit):" )
root.bind_all('<Key>', key)
# don't show the tk window
root.withdraw()
root.destroy
root.mainloop()
