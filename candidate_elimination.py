import tkinter as tk
from tkinter import messagebox
import numpy as np

class CandidateEliminationGUI:
    def __init__(self, root):
        self.root = root
        root.title("Candidate Elimination Algorithm")
        root.geometry("600x600")
        root.configure(bg="#f0f2f5")
        
        self.create_widgets()
        
        
        self.S = ['?'] * 5  
        self.G = [['?' for _ in range(5)] for _ in range(2)]  
    
    def create_widgets(self):
        # Labels and input fields for training data
        tk.Label(self.root, text="Enter Training Data (Comma-separated)", bg="#f0f2f5", font=("Arial", 12)).pack(pady=10)
        self.example_entry = tk.Entry(self.root, font=("Arial", 12))
        self.example_entry.pack(pady=5)
        
        tk.Label(self.root, text="Enter Class Label (1 for Positive, 0 for Negative)", bg="#f0f2f5", font=("Arial", 12)).pack(pady=10)
        self.label_entry = tk.Entry(self.root, font=("Arial", 12))
        self.label_entry.pack(pady=5)
        
        tk.Button(self.root, text="Add Example", command=self.add_example, font=("Arial", 12)).pack(pady=10)
        
        # S and G Hypotheses Display
        self.s_label = tk.Label(self.root, text="S (Specialized Hypothesis): ", bg="#f0f2f5", font=("Arial", 12))
        self.s_label.pack(pady=10)
        
        self.g_label = tk.Label(self.root, text="G (Generalized Hypothesis): ", bg="#f0f2f5", font=("Arial", 12))
        self.g_label.pack(pady=10)
        
        tk.Button(self.root, text="Start Elimination", command=self.start_elimination, font=("Arial", 12)).pack(pady=10)
    
    def add_example(self):
        # Get training example and class label
        example = self.example_entry.get().split(',')
        label = self.label_entry.get()

        if len(example) != 5 or label not in ['0', '1']:
            messagebox.showerror("Input Error", "Please enter a valid example (5 attributes, 0 or 1 as label).")
            return
        
        example = [x.strip() for x in example]
        label = int(label)
        
        # Update the hypotheses 
        self.update_hypotheses(example, label)
        
        # Update the display
        self.s_label.config(text=f"S (Specialized Hypothesis): {self.S}")
        self.g_label.config(text=f"G (Generalized Hypothesis): {self.G}")
        
        # Clear input fields
        self.example_entry.delete(0, tk.END)
        self.label_entry.delete(0, tk.END)

    def update_hypotheses(self, example, label):
        if label == 1:
            # Positive example: Update S (Specialized) and G (Generalized)
            for i in range(len(example)):
                if self.S[i] == '?':
                    self.S[i] = example[i]
                elif self.S[i] != example[i]:
                    self.S[i] = '?'
            
            new_G = []
            for hypothesis in self.G:
                if self.is_more_general_than_S(hypothesis):
                    new_G.append(hypothesis)
            
            self.G = new_G
        else:
            # Negative example: Update G (Generalized) and S (Specialized)
            for i in range(len(example)):
                if self.S[i] != example[i]:
                    self.G.append([example[i] if j == i else '?' for j in range(len(example))])
            
            new_S = []
            for hypothesis in self.G:
                if self.is_more_general_than_S(hypothesis):
                    new_S.append(hypothesis)
            
            self.S = new_S
    
    def is_more_general_than_S(self, hypothesis):
        for i in range(len(hypothesis)):
            if self.S[i] != '?' and self.S[i] != hypothesis[i]:
                return False
        return True
    
    def start_elimination(self):
        self.s_label.config(text=f"Final S (Specialized Hypothesis): {self.S}")
        self.g_label.config(text=f"Final G (Generalized Hypothesis): {self.G}")
        messagebox.showinfo("Elimination Complete", "Candidate Elimination process is complete.")

root = tk.Tk()
app = CandidateEliminationGUI(root)
root.mainloop()