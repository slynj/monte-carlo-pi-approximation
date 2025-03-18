import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000


def approximation():
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    inside_circle = x**2 + y**2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_samples

    return x, y, inside_circle, pi_estimate


def draw_circle(ax, num_samples):
    x, y, inside_circle, pi_estimate = approximation()

    ax.scatter(x[inside_circle], y[inside_circle], color='blue', s=1)
    ax.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f"pi = {pi_estimate:.5f} \nn = {num_samples}")


figure, axis = plt.subplots(3, 3, figsize=(8, 8))

for ax in axis.flatten():
    draw_circle(ax, num_samples)
    num_samples *= 2

plt.suptitle(f"Monte Carlo Pi Approximation", fontsize=18)
plt.subplots_adjust(hspace=0.6, wspace=0.6)

plt.savefig("pi-approximation.png")
plt.show()
