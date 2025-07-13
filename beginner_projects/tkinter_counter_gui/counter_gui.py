from tkinter import *

root = Tk()
root.geometry("420x450")
root.resizable(False, False)
root.title('Counter')

#VARIABLES
bgclr = "#DFCFCF"
count = 0

root.config(background=bgclr)


#FRAMES
display_frame = Frame(root,
                      bg = bgclr)
display_frame.pack(pady = 1, padx = 1)

button_frame = Frame(root,
                     bg = bgclr)
button_frame.pack(pady = 10)


#DISPLAY
display = Label(display_frame,
                bg = '#1A1A1A',
                width = 6,
                text = f'{count}',
                fg = '#00ff00',
                font = ('Arial', 60, 'bold'),
                relief = RAISED,
                bd = 5,
                padx = 15)
display.pack()

#FUNCTIONS


def background_color():
    '''
    Light and Dark modes.
    '''
    global bgclr
    if bgclr == '#DFCFCF':
        bgclr = '#121212'
        display_frame.config(bg = bgclr)
        button_frame.config(bg = bgclr)
        theme_button.config(bg = bgclr, fg = "#FFFFFF")
        increment_button.config(bg = bgclr, fg = "#FFFFFF")
        reset_button.config(bg = bgclr, fg = "#FFFFFF")
        root.config(bg = bgclr)
    else:
        bgclr = '#DFCFCF'
        display_frame.config(bg = bgclr)
        button_frame.config(bg = bgclr)
        theme_button.config(bg = bgclr, fg = "#000000")
        increment_button.config(bg = bgclr, fg = "#000000")
        reset_button.config(bg = bgclr, fg = "#000000")
        root.config(bg = bgclr)


def counter():
    '''
    Increment counter and update display.
    '''
    global count
    count += 1
    if count % 10000 == 0:
        count = 0
    display.config(text = f'{count}')


def reset():
    '''
    Reset the display to 0
    '''
    global count
    count = 0
    display.config(text = f'{count}')

# BUTTONS
theme_button = Button(display_frame,
               bg = bgclr,
               text = "Theme",
               command = background_color)
theme_button.pack()

increment_button = Button(button_frame,
                        bg = bgclr,
                        text = "Count +1",
                        font = ('Comic Sans', 25),
                        command = counter
                        )
increment_button.pack(pady = 50)

reset_button = Button(button_frame,
                      bg = bgclr,
                      text = 'Reset',
                      font = ('Comic Sans', 25),
                      command = reset
                      )
reset_button.pack(pady = 5)

root.mainloop()
