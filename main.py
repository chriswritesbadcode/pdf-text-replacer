import tkinter as tk
from tkinter import filedialog
from constants import *
from utils import *

window = tk.Tk()

window.title('PDF Text Replacer')
window.iconbitmap('favico.ico')
window.resizable(False,False)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - WINDOW_SIZE / 2)
position_right = int(screen_width / 2 - WINDOW_SIZE / 2)
window.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}+{position_right}+{position_top}')
window.protocol('WM_DELETE_WINDOW', lambda: on_close(window))

main_frame = tk.Frame(window, padx=FRAME_PAD, pady=FRAME_PAD)
main_frame.pack(expand=True, fill=tk.BOTH)
main_frame.configure(bg=WINDOW_BG)

generate_button = tk.Button(main_frame,
                   text='Generate new PDF',
                   command=lambda: generate_pdf(filedialog.askopenfilename(title='Select input PDF', filetypes=[('PDF', '.pdf')]), 'modified.pdf'))

generate_button.pack()


window.mainloop()