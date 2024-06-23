
import random
import re

def on_key_press(event, widget, original: str):
    """
    Parameters
    -----
    widget: user input tkinter Text widget

    original: example string
    """
    user_input = widget
    user_input.configure(state="normal")

    # Automatic scrolling of user input text field
    user_input.yview_scroll(1, "units")

    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = set("0123456789")

   # Writing letters and numbers
    if event.keysym in letters or event.keysym in numbers:
        write_symbol(widget, event.keysym, original)

    elif event.keysym == "space":
        user_input.insert("end", " ")

    elif event.keysym == "BackSpace":
        last_position = user_input.index("end-2c")
        user_input.delete(last_position, "end-1c")
    # Other keys
    else:
        handle_symbols(event, user_input, original)

    user_input.configure(state="disabled")


def handle_symbols(event, widget, original: str):
    """
    Parameters
    -----
    widget: user input tkinter Text widget

    original: example string
    """
    if event.keysym == "backslash":
        symbol = "\\"
    elif event.keysym == "comma":
        symbol = ","
    elif event.keysym == "period":
        symbol = "."
    elif event.keysym == "slash":
        symbol = "/"
    elif event.keysym == "semicolon":
        symbol = ";"
    elif event.keysym == "apostrophe":
        symbol = "'"
    elif event.keysym == "bracketleft":
        symbol = "["
    elif event.keysym == "bracketright":
        symbol = "]"
    elif event.keysym == "grave":
        symbol = "`"
    elif event.keysym == "minus":
        symbol = "-"
    elif event.keysym == "equal":
        symbol = "="
    elif event.keysym == "asterisk":
        symbol = "*"
    elif event.keysym == "plus":
        symbol = "+"
    elif event.keysym == "less":
        symbol = "<"
    elif event.keysym == "greater":
        symbol = ">"
    elif event.keysym == "question":
        symbol = "?"
    elif event.keysym == "bar":
        symbol = "|"
    elif event.keysym == "colon":
        symbol = ":"
    elif event.keysym == "quotedbl":
        symbol = '"'
    elif event.keysym == "braceleft":
        symbol = "{"
    elif event.keysym == "braceright":
        symbol = "}"
    elif event.keysym == "asciitilde":
        symbol = "~"
    elif event.keysym == "exclam":
        symbol = "!"
    elif event.keysym == "at":
        symbol = "@"
    elif event.keysym == "numbersign":
        symbol = "#"
    elif event.keysym == "dollar":
        symbol = "$"
    elif event.keysym == "percent":
        symbol = "%"
    elif event.keysym == "asciicircum":
        symbol = "^"
    elif event.keysym == "ampersand":
        symbol = "&"
    elif event.keysym == "parenleft":
        symbol = "("
    elif event.keysym == "parenright":
        symbol = ")"
    elif event.keysym == "underscore":
        symbol = "_"
    # Other keys
    else:
        return
    
    write_symbol(widget, symbol, original)


def count_words(input: str) -> int:
    words = input.split()
    return len(words)


def get_random_sentences(file_path: str, number: int) -> str|None:
    """
    Get random senteces from file.

    Parameters
    -----
    number: number of sentences to be taken

    Returns
    -----
    None if file could not be found
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        return None
    
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

    if len(sentences) < number:
        raise ValueError("The text file does not contain enough sentences.")
    
    # Choose random sentences
    selected_sentences = random.sample(sentences, number)
    
    result = ' '.join(selected_sentences)
    
    return result


def write_symbol(widget, symbol: str, original: str):
    """
    Writes symbol to the user input tkinter Text widget.
    Wrong symbols are written in red.

    Parameters
    -----
    widget: user input tkinter Text widget

    symbol: symbol that has to be written

    original: exaple string
    """
    user_input = widget

    # Adds new letter at the end
    user_input.insert("end", symbol, "black")

    words = user_input.get("1.0", "end-1c").split()
    original_words = original.split()
    
    # len() - 1 bcs indexes are from 0
    last_word_len = len(words[-1]) - 1
    if last_word_len < 0:
        last_word_len = 0

    # Input word has more symbols than the original
    if len(original_words[len(words) - 1]) < len(words[-1]):
        last_position = user_input.index("end-2c")
        user_input.delete(last_position, "end-1c")
        user_input.insert("end", symbol, "red")
        handle_typos("add")
    else:
        # Wrong symbol
        if symbol != original_words[len(words) - 1][last_word_len]:
            last_position = user_input.index("end-2c")
            user_input.delete(last_position, "end-1c")
            user_input.insert("end", symbol, "red")
            handle_typos("add")


def count_mistakes(widget, original: str) -> int:
    """
    Parameters
    -----
    widget: user input tkinter Text widget

    symbol: symbol that has to be written

    original: exaple string
    """
    user_input = widget
    # Get the ranges of text that have the "red" tag
    ranges = user_input.tag_ranges("red")
    
    count = 0
    
    # Iterate through the ranges and count the characters
    for i in range(0, len(ranges), 2):
        start = ranges[i]
        end = ranges[i + 1]
        count += len(user_input.get(start, end))

    # Forgotten symbols
    words = user_input.get("1.0", "end-1c").split()
    original_words = original.split()
    # User word is shorter than the original => user forgot some
    for i, word in enumerate(words):
        if len(word) < len(original_words[i]):
            count = count + len(original_words[i]) - len(word)

    return count

# Global typos count
typos = 0

def handle_typos(operation: str) -> int:
    """
    Parameters
    ----
    operation: 'add' / 'get'
    """
    global typos
    if operation == "add":
        typos += 1
    elif operation == "get":
        return typos
    else:
        raise Exception("Unexpected error")
    