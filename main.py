import tkinter as tk
import subprocess

def run_tic_tac_toe():
    subprocess.Popen(["python", "tic_tac_toe.py"])

def run_eight_puzzle():
    subprocess.Popen(["python", "8_puzzle.py"])

def run_water_jug():
    subprocess.Popen(["python", "water_jug.py"])

def run_candidate_elimination():
    subprocess.Popen(["python", "candidate_elimination.py"])

def run_backpropagation():
    subprocess.Popen(["python", "backpropogation.py"])

# Main window
root = tk.Tk()
root.title("AIML Experiments Desktop App")
root.geometry("400x400")
root.configure(bg="#f0f2f5")

tk.Label(root, text="Select an Experiment", font=("Arial", 16, "bold"), bg="#f0f2f5").pack(pady=20)

# Buttons for each experiment
tk.Button(root, text="1️⃣ Tic Tac Toe", command=run_tic_tac_toe, width=25, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="2️⃣ 8 Puzzle Problem", command=run_eight_puzzle, width=25, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="3️⃣ Water Jug Problem", command=run_water_jug, width=25, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="4️⃣ Candidate Elimination", command=run_candidate_elimination, width=25, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="5️⃣ Backpropagation", command=run_backpropagation, width=25, font=("Arial", 12)).pack(pady=5)

tk.Label(root, text="Created by Kamya Singh", font=("Arial", 10), bg="#f0f2f5", fg="#888").pack(side="bottom", pady=10)

root.mainloop()