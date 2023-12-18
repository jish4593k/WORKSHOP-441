import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import tkinter as tk
from tkinter import ttk


import torch

ers
r = 1.234240 
l = 4.24320  h
rot_num = 42342 
increment = 0.1T45t


torch_tensor = torch.randn(100)


angles = np.arange(0, rot_num * 2 * np.pi, increment)


sns.set(style="whitegrid")

def on_slider_change(val):
    current_frame = int(val)
    animate(current_frame)

root = tk.Tk()
root.title("Piston Motion Animation")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=20, pady=20)


frame_slider = ttk.Scale(frame, from_=0, to=len(angles) - 1, orient="horizontal", command=on_slider_change)
frame_slider.grid(row=0, column=0, columnspan=2)

label_slider = tk.Label(frame, text="Animation Frame:")
label_slider.grid(row=1, column=0, columnspan=2)


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(l+r)
line, = ax.plot([], [], "o-", lw=2, color="g")


sns.lineplot(x=range(len(torch_tensor)), y=torch_tensor.numpy(), ax=ax, color="blue")
ax.set_title('Seaborn Plot of Torch Tensor')


frame_slider.set(0)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta = angles[i]
    x1 = r * np.cos(theta)
    y1 = r * np.sin(theta)
    x2 = l * np.cos(theta - np.pi / 2)
    y2 = l * np.sin(theta - np.pi / 2)
    
    line.set_data([theta, theta], [0, l+r])
    frame_slider.set(i)  # Update the slider value
    return line,


ani = animation.FuncAnimation(fig, animate, frames=len(angles), init_func=init, blit=True)

root.mainloop()
