import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

from functions import count_words

def start_window(root, callback):

    def start():
        time = time_combobox.get()
        time = int(time) * 60
        callback(time)
        window.destroy()

    window = tk.Toplevel(root)
    window.geometry("400x200")
    window.title("Start up")
    window.after(100, window.lift)

    font = tkfont.Font(family="Helvetica", size=12)

    time_label = tk.Label(window, text="Set your time [minutes].", font=font)
    time_label.pack(pady=10)
    time_combobox = ttk.Combobox(window, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], font=font)
    time_combobox.set("1")
    time_combobox.pack(pady=10)

    start_button = tk.Button(window, text="Start", command=start, font=font)
    start_button.pack(pady=10)


def results_window(root, original: str, input: str, time: int):
    window = tk.Toplevel(root)
    window.geometry("400x200")
    window.title("Results")
    window.after(100, window.lift)

    font = tkfont.Font(family="Helvetica", size=12)
    
    # int() removes the decimal part => rouding down
    words_label = tk.Label(window, text=f"Number of words: {count_words(input)}", font=font)
    charakters_label = tk.Label(window, text=f"Number of charakters: {len(input)}", font=font)
    w_speed_label = tk.Label(window, text=f"Speed: {int(count_words(input) / (time / 60))} words/minute", font=font)
    c_speed_label = tk.Label(window, text=f"Speed: {int(len(input) / (time / 60))} charakters/minute", font=font)

    words_label.pack()
    charakters_label.pack()
    w_speed_label.pack()
    c_speed_label.pack()