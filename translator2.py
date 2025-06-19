import tkinter as tk
from tkinter import * 
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# GUI Set Up
root=Tk()
root.title("TEXT TO SPEECH")  # Window bar title (not stylable)
root.geometry("1200x600+200+100")
root.resizable(False, False)
root.config(bg="#F8DD67")

# Header Frame Box
frame = Frame(root, width=1200, height=75, bg="#1EBDCF")
frame.place(x=0, y=0) 

# Header Title
title_bar = Label(root,text=" ~ TRANSLATOR ~ ",font=("Times New Roman", 60, "bold"),fg="#000000",bg="#1EBDCF")
title_bar.place(x=330, y=3) 

# Decorative Line
divider = Frame(root, bg="#FA8E00", height=7, width=1200)
divider.place(x= 0, y = 75)

# Subheading
input_label = Label(root, text=" TEXT :", font=("Times New Roman", 45, "bold"), bg="#F8DD67" , fg="#000000")
input_label.place(x=180, y=90)

# Input Text Box
input_text = Text(root, font=("Times New Roman", 25, "bold"), wrap=WORD, height=13, width=40)
input_text.place(x=25, y=150)
input_text.focus_set()

# Language Selector
languages = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Korean": "ko",
    "Japanese": "ja"
}
language_names = {v: k for k, v in languages.items()}
selected_lang = tk.StringVar(value="Hindi")
lang_menu = OptionMenu(root, selected_lang, *languages.keys())
lang_menu.config(font=("Times New Roman", 25, "bold"))
lang_menu.place(x=850, y=100)

# Output Text Box
output_text = Text(root, font=("Times New Roman", 25, "bold"), wrap=WORD, height=13, width=40)
output_text.place(x=650, y=150)
output_text.configure(state='disabled')

# Global variable to store translated text
translated_text = ""

def translate_only():
    global translated_text
    text = input_text.get("1.0", END).strip()
    if not text:
        return
    try:
        target_code = languages[selected_lang.get()]
        translated_text = GoogleTranslator(source='auto', target=target_code).translate(text)
        output_text.configure(state='normal')
        output_text.delete("1.0", END)
        output_text.insert(END, translated_text)
        output_text.configure(state='disabled')
    except Exception as e:
        output_text.configure(state='normal')
        output_text.delete("1.0", END)
        output_text.insert(END, "Translation failed.")
        output_text.configure(state='disabled')

def speak_translated():
    global translated_text
    if translated_text:
        try:
            target_code = languages[selected_lang.get()]
            tts = gTTS(text=translated_text, lang=target_code)
            tts.save("output.mp3")
            os.system("afplay output.mp3")
        except Exception:
            output_text.configure(state='normal')
            output_text.delete("1.0", END)
            output_text.insert(END, "Speech failed.")
            output_text.configure(state='disabled')

translate_btn = Button(root, text=" TRANSLATE", font=("Times New Roman", 25, "bold"),
bg="#FFB347", fg="#000000", command=translate_only)
translate_btn.place(x=180, y=538)

speak_btn = Button(root, text= " SPEAK ", font=("Times New Roman", 25, "bold"),
bg="#FFB347", fg="#000000", command=speak_translated)
speak_btn.place(x=850, y=538)

root.mainloop()