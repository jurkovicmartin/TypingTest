import tkinter as tk
import time
import threading
from tkinter import font as tkfont
from tkinter import messagebox

from functions import on_key_press, get_random_sentences
from toplevel import results_window


def main():

    def start(seconds: int):
        """
        Stars the typing test.
        """
        global countdown_thread, original_string
        # Load random sentences from file
        original_string = get_random_sentences("example_text.txt", 10)
        # File doesn't exist
        if original_string is None:
            messagebox.showerror("File error", "Could not find 'example_text.txt' file, which contains example sentenses.")
            return
        # Show the sentences in the window
        original_text.configure(state="normal")
        original_text.delete("1.0", "end-1c")
        original_text.insert("1.0", original_string)
        original_text.configure(state="disabled")
        # Clear user input
        user_input.configure(state="normal")
        user_input.delete("1.0", "end-1c")
        user_input.configure(state="disabled")
        # Allow keyboard functionality
        root.bind("<KeyPress>", lambda event: on_key_press(event, user_input, original_string))
        # New threat for the countdown timer so it works parallely
        stop_flag.clear()
        countdown_thread = threading.Thread(target=countdown, args=(seconds,))
        countdown_thread.start()

        start_btn.configure(state="disabled")


    def countdown(seconds: int):
        save_time = seconds

        while seconds > -1:
            if stop_flag.is_set():
                return
            timer.configure(text=seconds)
            time.sleep(1)
            seconds -= 1
        # Countdown ends
        root.unbind("<KeyPress>")
        start_btn.configure(state="normal")
        # Show results
        results_window(root, original_string, save_time, user_input)


    def on_close():
        global countdown_thread
        try:
            # Closing the window before the timer expires
            # Killing the countdown thread
            stop_flag.set()
            countdown_thread.join()
        except NameError:
            # Closing the window without starting the timer
            pass
        finally:
            root.destroy()


    # Stop flag doesn't need global keyword bcs it is not reassigned (=)
    # It is only checked (read) and modified with methods
    stop_flag = threading.Event()

    # Main window
    root = tk.Tk()
    root.geometry("800x420")
    root.title("Typing speed test")

    font = tkfont.Font(family="Helvetica", size=12)
    
    # Timer
    timer = tk.Label(root, text="Timer", font=("Helvetica", 14, "bold"))
    timer.pack()
    # Example text
    original_text = tk.Text(root, wrap="word", width=80, height=15, spacing2=10, font=font)
    original_text.configure(state="disabled")
    original_text.pack()
    # User input text
    user_input = tk.Text(root, wrap="word", width=80, height=3, spacing2=10, font=font)
    user_input.tag_configure("red", foreground="red")
    user_input.tag_configure("black", foreground="black")
    user_input.configure(state="disabled")
    user_input.pack(pady=5)
    # Start button
    start_btn = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), command= lambda: start(60))
    start_btn.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", on_close)

    root.mainloop()



if __name__ == "__main__":
    main()