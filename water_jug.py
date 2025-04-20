import tkinter as tk
from tkinter import messagebox
import heapq

class WaterJugGUI:
    def __init__(self, root):
        self.root = root
        root.title("💧 Water Jug Problem")
        root.geometry("400x450")
        root.configure(bg="#f0f2f5")

        self.create_widgets()

    def create_widgets(self):
        # Input Section
        tk.Label(self.root, text="Jug 1 Capacity (L)", bg="#f0f2f5").pack(pady=5)
        self.jug1_entry = tk.Entry(self.root)
        self.jug1_entry.pack()

        tk.Label(self.root, text="Jug 2 Capacity (L)", bg="#f0f2f5").pack(pady=5)
        self.jug2_entry = tk.Entry(self.root)
        self.jug2_entry.pack()

        tk.Label(self.root, text="Goal (L)", bg="#f0f2f5").pack(pady=5)
        self.goal_entry = tk.Entry(self.root)
        self.goal_entry.pack()

        tk.Button(self.root, text="🧠 Solve", command=self.solve, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="🔁 Reset", command=self.reset, font=("Arial", 12)).pack(pady=5)

        self.output_box = tk.Text(self.root, height=12, width=40, wrap=tk.WORD, bg="#ffffff")
        self.output_box.pack(pady=10)

    def heuristic(self, state, goal):
        # Manhattan Distance Heuristic
        return abs(state[0] - goal) + abs(state[1] - goal)

    def get_possible_moves(self, state, cap1, cap2):
        x, y = state
        moves = [
            (cap1, y),  
            (x, cap2),  
            (0, y),     
            (x, 0),     
            (x - min(x, cap2 - y), y + min(x, cap2 - y)),  
            (x + min(y, cap1 - x), y - min(y, cap1 - x))   
        ]
        return list(set(moves))

    def solve(self):
        self.output_box.delete(1.0, tk.END)

        try:
            cap1 = int(self.jug1_entry.get())
            cap2 = int(self.jug2_entry.get())
            goal = int(self.goal_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers.")
            return

        start = (0, 0)
        goal_state = (goal, 0)

        # A* algorithm using priority queue
        visited = set()
        pq = []
        heapq.heappush(pq, (0 + self.heuristic(start, goal), 0, start, []))  # (f, g, state, path)

        while pq:
            f, g, current, path = heapq.heappop(pq)

            if current == goal_state:
                self.output_box.insert(tk.END, "✅ Solution Found!\n\n")
                for i, state in enumerate(path + [current]):
                    self.output_box.insert(tk.END, f"Step {i}: Jug1 = {state[0]}, Jug2 = {state[1]}\n")
                return

            if current in visited:
                continue
            visited.add(current)

            for move in self.get_possible_moves(current, cap1, cap2):
                if move not in visited:
                    heapq.heappush(pq, (g + 1 + self.heuristic(move, goal), g + 1, move, path + [current]))

        self.output_box.insert(tk.END, "❌ No solution found.\n")

    def reset(self):
        self.jug1_entry.delete(0, tk.END)
        self.jug2_entry.delete(0, tk.END)
        self.goal_entry.delete(0, tk.END)
        self.output_box.delete(1.0, tk.END)


root = tk.Tk()
app = WaterJugGUI(root)
root.mainloop()