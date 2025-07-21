import tkinter as tk
from tkinter import messagebox


#CONSTANTS
BACKGROUND_COLOR = '#121212'
LABEL_FONT = ('Consolas', 60, 'bold')
LABEL_BACKGROUND = '#1f1f1f'
LABEL_FOREGROUND = '#00FF00'
BUTTON_FONT = ('Consolas', 20, 'bold')
BUTTON_BG_COLOR = '#131313'
BUTTON_FG_COLOR = 'white'
#VARIABLES
count = 0


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
	
	
#GUI SETUPS
root = tk.Tk()
root.resizable(False, False)
root.title('Counter')

#FRAME
frame = tk.Frame(root, bg=BACKGROUND_COLOR)

#WIDGETS
#Lable/Display
label = tk.Label(frame, text=f'{count:05}', font=LABEL_FONT, bg=LABEL_BACKGROUND, fg=LABEL_FOREGROUND, width=6)

#Increment counter
increment_counter = tk.Button(frame, text='Count +1', font=BUTTON_FONT, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=counter_button)

#Increment reset
increment_reset = tk.Button(frame, text='Reset', font=BUTTON_FONT, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=reset_button)

#PLACING WIDGETS
frame.pack()
label.grid(row=0, column=0, columnspan=3, pady=15)
increment_counter.grid(row=1, column=0, columnspan=3, pady=15)
increment_reset.grid(row=2, column=0, columnspan=3, pady= 15)

root.mainloop()
