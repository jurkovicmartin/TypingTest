import tkinter as tk
import time
import threading
from tkinter import font as tkfont

from functions import on_key_press, get_random_sentences
from toplevels import start_window, results_window


def main():

    def time_callback(time):
        timer.configure(text=time)
        start(time)


    def start(seconds):
        original_text.configure(state="normal")
        original_text.insert("1.0", original_string)
        original_text.configure(state="disabled")

        countdown_thread = threading.Thread(target=countdown, args=(seconds,))
        countdown_thread.start()



    def countdown(seconds):
        save_time = seconds
        while seconds > -1:
            timer.configure(text=seconds)
            time.sleep(1)
            seconds -= 1

        root.unbind("<KeyPress>")
        results_window(root, original_string, user_input.get("1.0", "end-1c"), save_time)


    # Main window
    root = tk.Tk()
    root.geometry("800x400")
    root.title("Typing speed test")

    original_string = get_random_sentences("example_text.txt", 10)

    timer = tk.Label(root, text="Timer", font=("Helvetica", 14, "bold"))
    timer.pack()

    font = tkfont.Font(family="Helvetica", size=12)

    original_text = tk.Text(root, wrap="word", width=80, height=15, spacing2=10, font=font)
    original_text.configure(state="disabled")
    original_text.pack()

    user_input = tk.Text(root, wrap="word", width=80, height=3, spacing2=10, font=font)
    user_input.tag_configure("red", foreground="red")
    user_input.tag_configure("black", foreground="black")
    user_input.configure(state="disabled")
    user_input.pack(pady=5)

    root.bind("<KeyPress>", lambda event: on_key_press(event, user_input, original_string))

    start_window(root, time_callback)

    root.mainloop()



if __name__ == "__main__":
    main()