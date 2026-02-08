
import tkinter as tk
import random

user_score = 0
comp_score = 0
MAX_SCORE = 5

choices = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(list(choices.keys()))

    # Countdown animation
    result_label.config(text="Rock...")
    root.after(500, lambda: result_label.config(text="Paper..."))
    root.after(1000, lambda: result_label.config(text="Scissors..."))
    root.after(1500, lambda: show_result(user_choice, comp_choice))

def show_result(user_choice, comp_choice):
    global user_score, comp_score

    if user_choice == comp_choice:
        result = "It's a Tie!"
        color = "gray"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win! 🎉"
        color = "green"
        user_score += 1
    else:
        result = "Computer Wins! 🤖"
        color = "red"
        comp_score += 1

    result_label.config(
        text=f"You: {choices[user_choice]}    Computer: {choices[comp_choice]}\n{result}",
        fg=color
    )

    score_label.config(text=f"You: {user_score} | Computer: {comp_score}")

    if user_score == MAX_SCORE or comp_score == MAX_SCORE:
        winner = "YOU 🏆" if user_score == MAX_SCORE else "COMPUTER 🤖"
        result_label.config(text=f"{winner} WON THE GAME!", fg="purple")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def reset():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Choose your move!", fg="black")
    score_label.config(text="You: 0 | Computer: 0")
    for btn in buttons:
        btn.config(state=tk.NORMAL)

# --- UI ---
root = tk.Tk()
root.title("Rock Paper Scissors - Real Life Mode")
root.geometry("420x380")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

buttons = []
for move in choices:
    btn = tk.Button(
        btn_frame,
        text=f"{choices[move]}\n{move}",
        width=10,
        height=3,
        font=("Arial", 11),
        command=lambda m=move: play(m)
    )
    btn.pack(side=tk.LEFT, padx=6)
    buttons.append(btn)

result_label = tk.Label(root, text="Choose your move!", font=("Arial", 13))
result_label.pack(pady=15)

score_label = tk.Label(root, text="You: 0 | Computer: 0", font=("Arial", 11, "bold"))
score_label.pack(pady=10)

tk.Button(root, text="Restart Game", command=reset, fg="blue").pack(pady=10)

root.mainloop()
