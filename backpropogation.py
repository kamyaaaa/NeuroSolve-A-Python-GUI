import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier

class BackpropagationGUI:
    def __init__(self, root):
        self.root = root
        root.title("Backpropagation Neural Network")
        root.geometry("600x600")
        root.configure(bg="#f0f2f5")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter Number of Layers", bg="#f0f2f5", font=("Arial", 12)).pack(pady=10)
        self.layers_entry = tk.Entry(self.root, font=("Arial", 12))
        self.layers_entry.pack(pady=5)

        tk.Label(self.root, text="Enter Neurons per Layer", bg="#f0f2f5", font=("Arial", 12)).pack(pady=10)
        self.neurons_entry = tk.Entry(self.root, font=("Arial", 12))
        self.neurons_entry.pack(pady=5)

        tk.Label(self.root, text="Learning Rate", bg="#f0f2f5", font=("Arial", 12)).pack(pady=10)
        self.lr_entry = tk.Entry(self.root, font=("Arial", 12))
        self.lr_entry.pack(pady=5)

        tk.Button(self.root, text="Generate Random Data", command=self.generate_data, font=("Arial", 12)).pack(pady=10)

        tk.Button(self.root, text="🧠 Train Neural Network", command=self.train_network, font=("Arial", 12)).pack(pady=10)

        self.result_box = tk.Text(self.root, height=10, width=60, wrap=tk.WORD, bg="#ffffff", font=("Consolas", 10))
        self.result_box.pack(pady=10)

        self.plot_button = tk.Button(self.root, text="📊 Show Accuracy Plot", command=self.plot_accuracy, font=("Arial", 12))
        self.plot_button.pack(pady=10)

    def generate_data(self):
        try:
            self.X, self.y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, "Generated random data for classification.\n\n")
            self.result_box.insert(tk.END, f"Features: {self.X.shape[1]}, Samples: {self.X.shape[0]}\n")
        except Exception as e:
            messagebox.showerror("Data Error", str(e))

    def train_network(self):
        try:
            layers = int(self.layers_entry.get())
            neurons = int(self.neurons_entry.get())
            learning_rate = float(self.lr_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")
            return

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Standardize features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Initialize MLPClassifier with backpropagation
        self.nn = MLPClassifier(hidden_layer_sizes=(neurons,) * layers, max_iter=1000, learning_rate_init=learning_rate,
                                solver='adam', random_state=42, warm_start=True)

        # Train the model
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, "Training the neural network...\n")

        # Fit the model and capture training process for plotting
        self.train_accuracies = []
        for epoch in range(1, 1001):
            self.nn.fit(X_train, y_train)
            accuracy = self.nn.score(X_test, y_test)
            self.train_accuracies.append(accuracy)
            self.result_box.insert(tk.END, f"Epoch {epoch}: Accuracy = {accuracy * 100:.2f}%\n")
            self.root.update()  # Update the GUI during training
            if epoch % 100 == 0:
                self.result_box.insert(tk.END, "Epochs 100, 200, ... completed.\n")
                self.root.update()

        self.result_box.insert(tk.END, "Training completed!\n")

    def plot_accuracy(self):
        try:
            plt.plot(self.train_accuracies)
            plt.title("Accuracy Over Epochs")
            plt.xlabel("Epochs")
            plt.ylabel("Accuracy")
            plt.show()
        except Exception as e:
            messagebox.showerror("Plot Error", str(e))

root = tk.Tk()
app = BackpropagationGUI(root)
root.mainloop()