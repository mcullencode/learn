def centre_text(*args, sep = ' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text))//2
    print (" " * left_margin, text, file=file, flush=flush)

# *text signifies that there is a variable number of parameters

centre_text("first", "second", 3, 4, sep=':')

with open("centred", mode='w') as centred_file:
    centre_text("first", "second", 3, 4, sep=':')
    centre_text("spam and eggs")

try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter


def parabola(x):
    y = x * x
    return y

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width()/2
    y_origin = canvas.winfo_height()/2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')



mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x  in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()

print(repr(canvas))  #prints memory location