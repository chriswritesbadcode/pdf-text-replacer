import fitz
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
from constants import *

def on_close(window):
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        window.destroy()


def generate_pdf(input_pdf, output_pdf):    
    generateWindow = tk.Tk()
    mainFrame = tk.Frame(generateWindow, padx=FRAME_PAD, pady=FRAME_PAD)
    mainFrame.configure(bg=WINDOW_BG)
    
    doc = fitz.open(input_pdf)

    for page_num in range(len(doc)):
        page = doc[page_num]

        replaceListInput = tk.Text(mainFrame, width=20, height=2)
        
        replaceList = replaceListInput.get('1.0', 'end-1c').split(',')
        
        for replaceIitem in replaceList:            
            text_instances = page.search_for(replaceIitem)
            for inst in text_instances:
                page.add_redact_annot(inst, text=getInput(f'Enter input for {replaceIitem}'), fill=(1, 1, 1))
                page.apply_redactions()
            
    doc.save(output_pdf)
    doc.close()

    os.startfile(output_pdf)

    generateWindow.mainloop()


def getInput(prompt):
    window = tk.Tk()
    window.withdraw()

    input = simpledialog.askstring('Input', prompt)

    return input