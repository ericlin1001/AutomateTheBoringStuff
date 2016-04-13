import tkinter as tk

def onKeyPress(event):
    text.insert('end', "Pressed %s\n"%(event.char, ))

root = tk.Tk()
root.geometry('300x200');
text = tk.Text(root, background = 'black', foreground = 'white');
text.pack()
root.bind('<KeyPress>', onKeyPress);
root.mainloop();
