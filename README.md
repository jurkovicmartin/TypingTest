# TypingTest

Speed typing test with tkinter GUI.

User has **60 seconds** to rewrite as much text as possible. Example sentences are randomly taken from the **"example_text.txt"** file. Without this file the test won't start. As the user types, his mistakes are written in red. Detecting mistakes is word oriented so it is not done by simply comparing the original text to the user input. This comparison led to a problem that if the user forgot or added one symbol, the rest of his input was viewed as a mistake = not an ideal solution. The word based detecting fixed this issue.

Example sentences were generated using AI.

## Test results
- Number of words written
- Number of characters written
- Typing speed in words/s
- Typing speed in characters/s
- Mistakes in the written text
- Number of typos done in the process of writing
- Accuracy of typing (ration of typos and total characters)
