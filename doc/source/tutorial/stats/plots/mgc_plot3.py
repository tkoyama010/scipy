import numpy as np
import matplotlib.pyplot as plt


def mgc_plot(x, y, sim_name):
    """Plot sim and MGC-plot"""
    # simulation
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    ax.set_title(sim_name + " Simulation", fontsize=20)
    ax.scatter(x, y)
    ax.set_xlabel("X", fontsize=15)
    ax.set_ylabel("Y", fontsize=15)
    ax.axis("equal")
    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)
    plt.show()


np.random.seed(12345678)
unif = np.array(np.random.uniform(0, 5, size=100))
x = unif * np.cos(np.pi * unif)
y = unif * np.sin(np.pi * unif) + 0.4 * np.random.random(x.size)


mgc_plot(x, y, "Spiral")
