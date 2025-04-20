import tkinter as tk
from tkinter import messagebox
import heapq
import random
import copy

# Define goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Manhattan distance heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

# Find blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next possible states
def get_neighbors(state):
    i, j = find_blank(state)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            moves.append(new_state)
    return moves

# Greedy Best First Search
def gbfs(start_state):
    visited = set()
    heap = [(heuristic(start_state), start_state, [])]  # (heuristic, current_state, path)
    while heap:
        h, state, path = heapq.heappop(heap)
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if state == goal_state:
            return path + [state]
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (heuristic(neighbor), neighbor, path + [state]))
    return None

class EightPuzzleGUI:
    def __init__(self, root):
        self.root = root
        root.title("8 Puzzle - Greedy Best First Search")
        root.geometry("400x550")
        root.configure(bg="#f0f2f5")

        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]

        self.tiles = [[None]*3 for _ in range(3)]
        self.create_widgets()
        self.update_board()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Initial State", font=("Arial", 16, "bold"), bg="#f0f2f5")
        self.label.pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=("Helvetica", 24), width=4, height=2,
                                bg="white", fg="#333")
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.tiles[i][j] = btn

        control_frame = tk.Frame(self.root, bg="#f0f2f5")
        control_frame.pack(pady=20)

        tk.Button(control_frame, text="🔀 Randomize", font=("Arial", 12), command=self.randomize).grid(row=0, column=0, padx=10)
        tk.Button(control_frame, text="🧠 Solve GBFS", font=("Arial", 12), command=self.solve).grid(row=0, column=1, padx=10)
        tk.Button(control_frame, text="🔁 Reset", font=("Arial", 12), command=self.reset).grid(row=0, column=2, padx=10)

        self.status = tk.Label(self.root, text="", font=("Arial", 12), bg="#f0f2f5", fg="#333")
        self.status.pack(pady=10)

    def update_board(self, board=None):
        if board:
            self.board = board
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                self.tiles[i][j].config(text=str(val) if val != 0 else "")

    def randomize(self):
        nums = list(range(9))
        random.shuffle(nums)
        self.board = [nums[i*3:(i+1)*3] for i in range(3)]
        self.update_board()
        self.status.config(text="")

    def solve(self):
        self.status.config(text="Solving...")
        self.root.update()
        result = gbfs(self.board)
        if result:
            self.status.config(text=f"Steps to goal: {len(result)-1}")
            self.animate_solution(result)
        else:
            self.status.config(text="❌ No solution found.")

    def animate_solution(self, steps):
        for state in steps:
            self.update_board(state)
            self.root.update()
            self.root.after(500)

    def reset(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 0]]
        self.update_board()
        self.status.config(text="")

root = tk.Tk()
app = EightPuzzleGUI(root)
root.mainloop()