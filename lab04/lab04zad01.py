import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

max_bound = np.ones(6)
min_bound = np.zeros(6)
bounds = (min_bound, max_bound)

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6, options=options, bounds=bounds)

def endurance(x):
    return np.exp(-2 * (x[:, 1] - np.sin(x[:, 0])) ** 2) + np.sin(x[:, 2] * x[:, 3]) + np.cos(x[:, 4] * x[:, 5])
    # return np.sum(np.power(np.abs(x), np.abs(x+1)), axis=1)

def f(x):
    return -1 * endurance(x)

optimizer.optimize(f, iters=100)

print("best cost:", optimizer.cost_history[-1])
print("best pos:", optimizer.pos_history[-1])

plot_cost_history(optimizer.cost_history)
plt.show()