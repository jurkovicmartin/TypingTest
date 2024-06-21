
import random
import re


def on_key_press(event, widget, original: str):
    user_input = widget
    user_input.configure(state="normal")

    # Automatic scrolling
    user_input.yview_scroll(1, "units")

    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = set("0123456789")

    text = user_input.get("1.0", "end-1c")
   
    if event.keysym in letters or event.keysym in numbers:
        if event.keysym != original[len(text)]:
            user_input.insert("end", event.keysym, "red")
        else:
            user_input.insert("end", event.keysym, "black")

    elif event.keysym == "space":
        user_input.insert("end", " ")

    elif event.keysym == "BackSpace":
        user_input.delete("1.0", "end")
        # Keeping the colors
        for i in range(0, len(text) - 1):
            if text[i] != original[i]:
                user_input.insert("end", text[i], "red")
            else:
                user_input.insert("end", text[i], "black")

        # After rewriting scroll to bottom
        user_input.see("end")

    else:
        handle_symbols(event, user_input, text, original)

    user_input.configure(state="disabled")


def handle_symbols(event, user_input, text: str, original: str):
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
    
    # Write the symbol
    if symbol != original[len(text)]:
        user_input.insert("end", symbol, "red")
    else:
        user_input.insert("end", symbol, "black")


def count_words(input: str) -> int:
    words = input.split()
    return len(words)


def get_random_sentences(file_path, number):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)

    if len(sentences) < number:
        raise ValueError("The text file does not contain enough sentences.")
    
    selected_sentences = random.sample(sentences, number)
    
    result = ' '.join(selected_sentences)
    
    return result
    