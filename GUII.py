import tkinter
import customtkinter
from mainn import word, check_guess, attempts, already_guessed_letters
import random


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Root window
root = customtkinter.CTk()
root.geometry("900x700")

# Function for game logic 
def check_guess(word, guess, attempts, already_guessed_letters):
    correct_placement = []
    wrong_placement = []
    
    # Step 1: Check for correct letters in the right position
    for i in range(len(word)):
        if word[i] == guess[i]:  # Correct letter and position
            correct_placement.append(guess[i])
        elif guess[i] in word and guess[i] not in correct_placement and guess[i] not in wrong_placement:
            # Step 2: If the letter is in the word but not in the correct position
            wrong_placement.append(guess[i])

    # Step 3: Update already guessed letters
    already_guessed_letters.extend([letter for letter in guess if letter not in already_guessed_letters])

    if guess == word:
        return "win", (correct_placement, wrong_placement, already_guessed_letters, attempts)
    elif attempts >= 6:  # If we've reached max attempts
        return "lose", (correct_placement, wrong_placement, already_guessed_letters, attempts)
    else:
        return "continue", (correct_placement, wrong_placement, already_guessed_letters, attempts)


def handle_guess():
    global attempts, already_guessed_letters
    guess = entry_game.get().strip()
    
    # Validate word length
    if len(guess) != 5:
        result_label.configure(fg_color = "white", text="Please enter a 5-letter word!")
        return
    
    attempts += 1  # Increment attempts after each guess
    result, feedback = check_guess(word, guess, attempts, already_guessed_letters)

    if result == "win":
        result_label.configure(text="Congratulations! You've guessed the word!")
        disable_game()
    elif result == "lose":
        result_label.configure(text=f"Sorry, you've lost. The correct word was: {word}")
        disable_game()
    elif result == "continue":
        correct_placement, wrong_placement, already_guessed, attempts = feedback
        result_label.configure(text=f"Correct Placement: {correct_placement}\nWrong placement: {wrong_placement}\nAlready guessed: {already_guessed}")
        update_grid(guess, correct_placement, wrong_placement)
    
    entry_game.delete(0, "end")


def disable_game():
    entry_game.configure(state="disabled")
    enter_button.configure(state="disabled")


def update_grid(guess, correct_placement, wrong_placement):
    for i, letter in enumerate(guess):
        # Apply color based on correct or wrong placement
        if letter in correct_placement:
            grid[attempts - 1][i].configure(text=letter, fg_color="green", font = ("Ariel", 18))
            correct_placement.remove(letter)  # Remove letter to avoid processing it again
        elif letter in wrong_placement:
            grid[attempts - 1][i].configure(text=letter, fg_color="orange", font = ("Ariel", 18))
            wrong_placement.remove(letter)  # Remove letter to avoid processing it again
        else:
            grid[attempts - 1][i].configure(text=letter, fg_color="grey", text_color = "black", font = ("Ariel", 18))


# Function to manage frame switching
def next_frame(current_frame, next_frame):
    current_frame.pack_forget()  # Hide the current frame
    next_frame.pack(pady=20, padx=60, fill="both", expand=True)  # Show the next frame

# Frame 1: Main Menu
frame_main = customtkinter.CTkFrame(master=root)
frame_main.pack(pady=20, padx=60, fill="both", expand=True)

label_main = customtkinter.CTkLabel(master=frame_main, text="Twordle", font=("Impact", 24))
label_main.pack(pady=12, padx=10)

label_instructions = customtkinter.CTkLabel(master=frame_main, text="Hello and welcome to Twordle! \nThis game was made during our 2024 Destin, FL trip \nbecause we were bored and decided to code our boredom away.\n", font=("Ariel", 16))
label_instructions.pack(pady = 12, anchor = "n")

continue_button = customtkinter.CTkButton(master=frame_main, text="Continue", command=lambda: next_frame(frame_main, frame_game))
continue_button.pack(pady=12, padx=10)

quit_button = customtkinter.CTkButton(master=frame_main, text = "Quit", fg_color= '#EA0000', hover_color = '#B20000', command=root.destroy)
quit_button.pack(pady = 12, padx = 10)

# Frame 2: Game Screen
frame_game = customtkinter.CTkFrame(master=root)

label_game = customtkinter.CTkLabel(master=frame_game, text="Twordle", font=("Impact", 24))
label_game.pack(pady=12, anchor = "n")

grid_frame = customtkinter.CTkFrame(master=frame_game)
grid_frame.pack(pady=10, anchor="n")

entry_game = customtkinter.CTkEntry(master=frame_game, placeholder_text="Enter Word")
entry_game.pack(pady=12, padx=10)

entry_game.bind("<Return>", lambda event: handle_guess())

enter_button = customtkinter.CTkButton(master=frame_game, text="Enter", command=handle_guess)
enter_button.pack(pady=12, padx=10)

back_button = customtkinter.CTkButton(master=frame_game, text="Back", command=lambda: next_frame(frame_game, frame_main))
back_button.pack(pady=12, padx=10)

quit_button = customtkinter.CTkButton(master=frame_game, text = "Quit", fg_color= '#EA0000', hover_color = '#B20000', command=root.destroy)
quit_button.pack(pady = 12, padx = 10)

result_label = customtkinter.CTkLabel(master=frame_game, text="", text_color="black")
result_label.pack(pady=12)

# grid making
grid = []
for i in range(6):
    row = []
    for j in range(5):
        label_grid = customtkinter.CTkLabel(master=grid_frame, text="", width=50, height=50, fg_color="grey")
        label_grid.grid(row=i, column=j, padx=5, pady=5)
        row.append(label_grid)
    grid.append(row)

# Start the application
root.mainloop()
