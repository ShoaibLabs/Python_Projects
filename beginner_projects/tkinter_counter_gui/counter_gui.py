import tkinter as tk
from tkinter import messagebox


#CONSTANTS
LABEL_FONT = ('Consolas', 60, 'bold')
BUTTON_FONT = ('Consolas', 20, 'bold')
BUTTON_FG_COLOR = 'white'
#Dark Theme
DARK_THEME = {
    'BACKGROUND_COLOR': '#121212',
    'LABEL_BACKGROUND': '#1f1f1f',
    'LABEL_FOREGROUND': '#00FF00',
    'BUTTON_BG_COLOR': '#131313',
    'BUTTON_FG_COLOR': 'white',
    'THEME_ICON': '🔆'
}
#Light theme
LIGHT_THEME = {
    'BACKGROUND_COLOR': '#FAFAFA',
    'LABEL_BACKGROUND': '#FFFFFF',
    'LABEL_FOREGROUND': '#1A237E',
    'BUTTON_BG_COLOR': '#E8EAF6',
    'BUTTON_FG_COLOR': '#1A237E',
    'THEME_ICON': '🌙'
}

#VARIABLES
count = 0
current_theme = DARK_THEME


#FUNCTIONS
#Count +1
def counter_button():
    global count
    
    count += 1
    
    label['text'] = f'{count:05}'
    
    if count % 10000 == 0:
        messagebox.showinfo(title='Counter', message='You have hit the limit')
        reset_button()
        return

#Reseting the count
def reset_button():
    global count
    
    count = 0
    
    label['text'] = f'{count:05}'
    

#Theme change
def theme_change():
    global current_theme
    
    if current_theme == DARK_THEME:
        current_theme = LIGHT_THEME
    else:
        current_theme = DARK_THEME
    
     # Apply theme to all widgets
    frame.config(bg=current_theme['BACKGROUND_COLOR'])
    label.config(bg=current_theme['LABEL_BACKGROUND'],
                 fg=current_theme['LABEL_FOREGROUND'])

    increment_counter.config(bg=current_theme['BUTTON_BG_COLOR'],
                             fg=current_theme['BUTTON_FG_COLOR'])
    increment_reset.config(bg=current_theme['BUTTON_BG_COLOR'],
                           fg=current_theme['BUTTON_FG_COLOR'])
    theme_button.config(bg=current_theme['BUTTON_BG_COLOR'],
                        fg=current_theme['BUTTON_FG_COLOR'],
                        text=current_theme['THEME_ICON'])
    
    
#GUI SETUPS
root = tk.Tk()
root.resizable(False, False)
root.title('Counter')

#FRAME
frame = tk.Frame(root, bg=DARK_THEME['BACKGROUND_COLOR'])

#WIDGETS
#Lable/Display
label = tk.Label(frame, text=f'{count:05}', font=LABEL_FONT, bg=DARK_THEME['LABEL_BACKGROUND'], fg=DARK_THEME['LABEL_FOREGROUND'], width=6)

#Increment counter
increment_counter = tk.Button(frame, text='Count +1', font=BUTTON_FONT, bg=DARK_THEME['BUTTON_BG_COLOR'], fg=DARK_THEME['BUTTON_FG_COLOR'], command=counter_button)

#Increment reset
increment_reset = tk.Button(frame, text='Reset', font=BUTTON_FONT, bg=DARK_THEME['BUTTON_BG_COLOR'], fg=DARK_THEME['BUTTON_FG_COLOR'], command=reset_button)

#Theme button
theme_button = tk.Button(frame, text=DARK_THEME['THEME_ICON'], font=BUTTON_FONT, bg=DARK_THEME['BUTTON_BG_COLOR'], width=5, command=theme_change)

#PLACING WIDGETS
frame.pack()
label.grid(row=0, column=0, columnspan=3, pady=15)
increment_counter.grid(row=1, column=0, columnspan=3, pady=10, sticky='ew')
increment_reset.grid(row=2, column=0, pady= 15)
theme_button.grid(row=2, column=2, pady = 15)

root.mainloop()
