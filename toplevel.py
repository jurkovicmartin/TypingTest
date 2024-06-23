import tkinter as tk
from tkinter import font as tkfont

from functions import count_words, count_mistakes, handle_typos

def results_window(root, original: str, time: int, widget):
    """
    Toplevel window to show final results.

    Parameters
    -----
    original: original exaple text

    time: time of the test [s]

    widget: user input tkinter Text widget
    """
    window = tk.Toplevel(root)
    window.geometry("400x200")
    window.title("Results")
    window.after(100, window.lift)

    font = tkfont.Font(family="Helvetica", size=12)
    # User input string
    input = widget.get("1.0", "end-1c")

    # Empty input field
    if len(input) == 0:
        accuracy = 0.0
    else:
        accuracy = (len(input) - handle_typos("get")) / len(input) * 100
    # Case of too many typos (typos > symbols)
    if accuracy < 0:
        accuracy = 0.0
    
    # int() removes the decimal part => rounding down
    words_label = tk.Label(window, text=f"Number of words: {count_words(input)}", font=font)
    characters_label = tk.Label(window, text=f"Number of characters: {len(input)}", font=font)
    w_speed_label = tk.Label(window, text=f"Speed: {int(count_words(input) / (time / 60))} words/minute", font=font)
    c_speed_label = tk.Label(window, text=f"Speed: {int(len(input) / (time / 60))} characters/minute", font=font)
    mistakes_label = tk.Label(window, text=f"Total mistakes: {count_mistakes(widget, original)}", font=font)
    typos_label = tk.Label(window, text=f"Total typos: {handle_typos('get')}", font=font)
    accuracy_label = tk.Label(window, text=f"Accuracy: {int(accuracy)} %", font=font)

    words_label.pack()
    characters_label.pack(pady=(0, 5))
    w_speed_label.pack()
    c_speed_label.pack(pady=(0, 5))
    mistakes_label.pack()
    typos_label.pack()
    accuracy_label.pack()