from tkinter import *

app = Tk()
app.title('Alfreds world')
app.geometry("800x500+100+25")
canvas = Canvas(app, height=500,width=800)
character = PhotoImage(file = "C:\Python Code 2012\Alfred's World\Smiley2.gif")
character_x = 500
character_y = 150
character_object = canvas.create_image(character_x, character_y, anchor=NE, image=character)
canvas.pack()

def key(event):
    if event.keysym == 'Escape':
        app.destroy()
    if event.char == event.keysym:
     # normal number and letter characters
        global character_x, character_y
        print( 'Normal Key %r' % event.char )
        if event.keysym == 'w':
            character_y -= 4
            canvas.coords(character_object, character_x, character_y)
        if event.keysym == 's':
            character_y += 4
            canvas.coords(character_object, character_x, character_y)
        if event.keysym == 'a':
            character_x -= 4
            canvas.coords(character_object, character_x, character_y)
        if event.keysym == 'd':
            character_x += 4
            canvas.coords(character_object, character_x, character_y)
    elif len(event.char) == 1:
      # charcters like []/.,><#$ also Return and ctrl/key
        print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
    else:
      # f1 to f12, shift keys, caps lock, Home, End, Delete ...
        print( 'Special Key %r' % event.keysym )


print( "Press a key (Escape key to exit):" )
app.bind_all('<Key>', key)
# don't show the tk window
app.mainloop()
