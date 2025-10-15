import tkinter as tk
from itertools import permutations
import math

class RouteOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Route Optimization Tool")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.machines = []   # List of (x, y) positions
        self.machine_circles = []
        self.lines = []

        self.info_label = tk.Label(root, text="Click to add machines. Click 'Optimize Route' when ready.")
        self.info_label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.optimize_btn = tk.Button(self.button_frame, text="Optimize Route", command=self.optimize_route)
        self.optimize_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        self.canvas.bind("<Button-1>", self.add_machine)

    def add_machine(self, event):
        x, y = event.x, event.y
        r = 8
        circle = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="skyblue", outline="black")
        label = self.canvas.create_text(x, y-12, text=f"M{len(self.machines)+1}", font=("Arial", 8))
        self.machines.append((x, y))
        self.machine_circles.append((circle, label))

    def distance(self, p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def total_distance(self, path):
        return sum(self.distance(path[i], path[i+1]) for i in range(len(path)-1))

    def optimize_route(self):
        if len(self.machines) < 2:
            self.info_label.config(text="Add at least two machines!")
            return

        # Remove previous lines
        for line in self.lines:
            self.canvas.delete(line)
        self.lines.clear()

        best_path = None
        best_distance = float("inf")

        for perm in permutations(self.machines):
            dist = self.total_distance(perm)
            if dist < best_distance:
                best_distance = dist
                best_path = perm

        # Draw optimized route
        for i in range(len(best_path)-1):
            line = self.canvas.create_line(
                best_path[i][0], best_path[i][1],
                best_path[i+1][0], best_path[i+1][1],
                fill="red", width=2
            )
            self.lines.append(line)

        self.info_label.config(text=f"Optimized route distance: {best_distance:.2f}")

    def reset(self):
        self.canvas.delete("all")
        self.machines.clear()
        self.machine_circles.clear()
        self.lines.clear()
        self.info_label.config(text="Click to add machines. Click 'Optimize Route' when ready.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RouteOptimizer(root)
    root.mainloop()
