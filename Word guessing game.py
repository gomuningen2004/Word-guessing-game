import tkinter as tk
import random
import time
from tkinter import messagebox

# Function to choose a word
def choose_word():
    words = [
        "python", "java", "swift", "javascript", "ruby", "kotlin", "html", "css",
        "c", "c++", "c#", "php", "typescript", "go", "rust", "scala", "perl",
        "dart", "objective-c", "sql", "groovy", "haskell", "lua", "matlab", "fortran",
        "cobol", "ada", "scheme", "prolog", "lisp", "f#", "ocaml", "erlang", "elixir",
        "clojure", "bash", "powershell", "assembly", "smalltalk", "delphi",
        "julia", "coffeescript", "verilog", "racket", "elm", "chapel", "d", "pl/sql", "tcl"
    ]
    return random.choice(words)

# Function to handle the player's guess
def guess_word():
    global attempts, start_time, word_to_guess, guessed_letters
    guess = letter_guess.get().lower()
    
    if not guess:
        messagebox.showwarning("No Input", "Please enter a word to guess.")
        return
    
    if guess == word_to_guess:
        response1 = messagebox.askyesno("Congratulations!", "You guessed the word!\nDo you want to play again?")
        if response1:
            reset_game()
        else:
            root.destroy()
    else:
        if guess not in guessed_letters:
            guessed_letters.extend([letter for letter in guess if letter in word_to_guess])
        attempts -= 1
        attempts_left.set(f"Attempts left: {attempts}")
        if attempts == 0:
            response2 = messagebox.askyesno("Out of attempts", f"The word was {word_to_guess}.\nDo you want to play again?")
            if response2:
                reset_game()
            else:
                root.destroy()
        else:
            display = display_word(word_to_guess, guessed_letters)
            word_display.set(display)

# Function to provide a hint about the word
def hint():
    messagebox.showinfo("Hint", f"The word starts with: {word_to_guess[0]}")

# Function to play the game again
def play_again():
    global word_to_guess, attempts, start_time, guessed_letters
    word_to_guess = choose_word()
    attempts = 6
    start_time = time.time()
    guessed_letters = []
    
    word_display.set(display_word(word_to_guess, guessed_letters))
    attempts_left.set(f"Attempts left: {attempts}")

# Function to reset the game
def reset_game():
    play_again()
    letter_guess.set("")  # Clear the Entry widget

# Function to display the word with correctly guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

# Initial setup
word_to_guess = choose_word()
guessed_letters = []
attempts = 6

# Create the GUI
root = tk.Tk()
root.title("Wordle Game")

# Styling
root.geometry("400x300")
root.configure(bg="#F8E5E5")

word_display = tk.StringVar()
word_display.set(display_word(word_to_guess, guessed_letters))

attempts_left = tk.StringVar()
attempts_left.set(f"Attempts left: {attempts}")

letter_guess = tk.StringVar()

word_label = tk.Label(root, textvariable=word_display, font=("Arial", 20), bg="#F8E5E5")
word_label.pack(pady=20)

attempts_label = tk.Label(root, textvariable=attempts_left, font=("Arial", 12), bg="#F8E5E5")
attempts_label.pack()

guess_entry = tk.Entry(root, textvariable=letter_guess, font=("Arial", 12))
guess_entry.pack(pady=10, padx=10)  # Adjust padx to add space

button_frame = tk.Frame(root, bg="#F8E5E5")  # Create a frame for buttons
button_frame.pack()

guess_button = tk.Button(button_frame, text="Guess", command=guess_word, font=("Arial", 12), bg="#FFD700", fg="black")
guess_button.pack(side=tk.LEFT, padx=5)

hint_button = tk.Button(button_frame, text="Hint", command=hint, font=("Arial", 12), bg="#ADD8E6", fg="black")
hint_button.pack(side=tk.LEFT, padx=5)

play_again_button = tk.Button(button_frame, text="Refresh", command=play_again, font=("Arial", 12), bg="#ADD8E6", fg="black")
play_again_button.pack(side=tk.LEFT, padx=5)

quit_button = tk.Button(button_frame, text="Quit", command=root.destroy, font=("Arial", 12), bg="#ADD8E6", fg="black")
quit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
