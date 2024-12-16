from tkinter import Tk, Label, Entry, Button, messagebox
from gtts import gTTS
import os
def play_speech():
    text = text_entry.get().strip()
    if not text:
        messagebox.showerror("Error", "Please enter text to convert to speech.")
        return
    try:
        tts = gTTS(text, lang='ar')
        tts.save("temp_audio.mp3")
        os.system("start temp_audio.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while playing audio: {e}")
def clear_text():
    text_entry.delete(0, 'end')
def exit_program():
    root.destroy()
root = Tk()
root.title("Text-to-Speech Program")
root.geometry("400x150")
Label(root, text="Enter Your Text:", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)
text_entry = Entry(root, font=("Arial", 12), width=40)
text_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
Button(root, text="Play", command=play_speech, font=("Arial", 12)).grid(row=2, column=0, padx=1, pady=10)
Button(root, text="Exit", command=exit_program, font=("Arial", 12), bg="red", fg="white").grid(row=2, column=1, padx=1)
Button(root, text="Set", command=clear_text, font=("Arial", 12)).grid(row=2, column=2, padx=1)
root.mainloop()