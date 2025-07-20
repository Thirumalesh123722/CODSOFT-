import tkinter as tk
import random

user_score = 0
comp_score = 0

def play(choice):
    global user_score, comp_score

    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    result = ""
    if choice == computer:
        result = "It's a Tie!"
    elif (choice == "rock" and computer == "scissors") or \
         (choice == "scissors" and computer == "paper") or \
         (choice == "paper" and computer == "rock"):
        user_score += 1
        result = "You Win!"
    else:
        comp_score += 1
        result = "Computer Wins!"

    result_label.config(text=f"You: {choice}   Computer: {computer}\n{result}")
    score_label.config(text=f"Score ➤ You: {user_score} | Computer: {comp_score}")

# GUI Window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game 🎮")
window.geometry("400x300")
window.config(bg="#e0f7fa")

tk.Label(window, text="Choose Your Move:", font=("Arial", 14), bg="#e0f7fa").pack(pady=10)

# Buttons
tk.Button(window, text="Rock", command=lambda: play("rock"), width=10).pack(pady=2)
tk.Button(window, text="Paper", command=lambda: play("paper"), width=10).pack(pady=2)
tk.Button(window, text="Scissors", command=lambda: play("scissors"), width=10).pack(pady=2)

# Result Display
result_label = tk.Label(window, text="", font=("Arial", 12), bg="#e0f7fa")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score ➤ You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#e0f7fa")
score_label.pack(pady=5)

window.mainloop()