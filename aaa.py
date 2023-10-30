import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import pandas as pd
import difflib

# Load your Marathi word frequency dataset
data = pd.read_csv("marathi_word.csv")

# Extract Marathi words from the dataset
marathi_words = set(data["Marathi_Word"])

# Create a function to check Marathi spellings
def check_marathi_spelling():
    input_text = text_widget.get("1.0", "end-1c")  # Get the text from the GUI input
    words = input_text.split()
    
    misspelled_words = []
    suggestions = []
    
    for word in words:
        # Remove common punctuation marks
        word = word.strip('.,!?()[]{}"\'')
        
        if word and word not in marathi_words:
            misspelled_words.append(word)
            # Find similar words from the dataset as suggestions
            close_matches = difflib.get_close_matches(word, marathi_words)
            suggestions.extend(close_matches)
    
    if misspelled_words:
        misspelled_text = ", ".join(misspelled_words)
        correction_text = ", ".join(suggestions) if suggestions else "No suggestions available."
        message = f"Misspelled words: {misspelled_text}\nSuggestions: {correction_text}"
        messagebox.showwarning("Spelling Check", message)
    else:
        messagebox.showinfo("Spelling Check", "No misspelled words found!")

# Create a GUI window
root = tk.Tk()
root.title("Marathi Spelling Checker")

# Create a text widget for input
text_widget = scrolledtext.ScrolledText(root, width=40, height=10)
text_widget.pack()

# Create a Check Spelling button
check_button = tk.Button(root, text="Check Spelling", command=check_marathi_spelling)
check_button.pack()

# Run the GUI main loop
root.mainloop()
