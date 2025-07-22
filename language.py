"""
    Language selection module for Python GUI apps using Tkinter.
    
    - Stores the language selection in a binary `.dat` file
    - Default file: lang.dat, saved using `pickle`
    - Default language selection is between English and Arabic, English = 0, Arabic = 1 
    - Skips the language window if a choice already exists.
"""

import pickle
import os
from tkinter import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_FILE = os.path.join(SCRIPT_DIR, "lang.dat")

# This function gets you the saved language code, (Expected output: 0 or 1)
def get_saved_language():
    if os.path.exists(LANG_FILE):
        try:
            with open(LANG_FILE, 'rb') as f:
                return pickle.load(f)
        except:
            return None
    return None

def save_language(language_code):
    with open(LANG_FILE, 'wb') as f:
        pickle.dump(language_code, f)

# This function lets you choose between the (two) languages
def langChoice():
    # Skip if already selected
    if get_saved_language() is not None:
        return

    def disable_event():
        pass

    langwindow = Tk()
    langwindow.geometry("400x200")
    langwindow.title("Choose Your Language")
    langwindow.resizable(False, False)
    langwindow.protocol("WM_DELETE_WINDOW", disable_event)
    langwindow.config(bg="#f0f8ff")  # Light blue background

    title = Label(langwindow,
                  text="🌍 Choose Your Language",
                  font=("Arial", 20, "bold"),
                  fg="#333",
                  bg="#f0f8ff")
    title.pack(pady=20)

    def choose(language_code):
        save_language(language_code)
        langwindow.destroy()

    btn_frame = Frame(langwindow, bg="#f0f8ff")
    btn_frame.pack(pady=10)

    EngBtn = Button(btn_frame,
                    text="English",
                    width=12,
                    bg="#4caf50",
                    fg="white",
                    activebackground="#45a049",
                    font=("Segoe UI", 13),
                    relief="raised",
                    command=lambda: choose(0))
    EngBtn.pack(side=LEFT, padx=15)

    ArbBtn = Button(btn_frame,
                    text="العربية",
                    width=12,
                    bg="#2196f3",
                    fg="white",
                    activebackground="#1e88e5",
                    font=("Segoe UI", 13),
                    relief="raised",
                    command=lambda: choose(1))
    ArbBtn.pack(side=LEFT, padx=15)

    langwindow.mainloop()

# This function clears the file if the user wants to reset
def langClear():
    if os.path.exists(LANG_FILE):
        os.remove(LANG_FILE)



if __name__ == "__main__":
    langChoice()
