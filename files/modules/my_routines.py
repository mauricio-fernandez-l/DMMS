import numpy as np
import matplotlib.pyplot as plt

# %% 

colors = ['blue', 'orange', 'green', 'red']

def plot_strain_stress(strain, stress, stress_model=[]):
    plt.figure()
    for i in range(4):
        x = np.linalg.norm(strain[9*i:9*(i+1)], axis=1)    
        f = np.linalg.norm(stress[9*i:9*(i+1)], axis=1)
        plt.plot(x, f, color=colors[i], label='path %i - data' % (i+1), linestyle='--')
        plt.scatter(x, f, color=colors[i])
        if len(stress_model) > 0:
            f_m = np.linalg.norm(stress_model[9*i:9*(i+1)], axis=1)
            plt.plot(x, f_m, color=colors[i], label='path %i - model' % (i+1))
    plt.xlabel('$||\\varepsilon||$')
    plt.ylabel('$||\\sigma||$')
    plt.legend()
    plt.show()
    
def plot_loss(h):
    plt.figure()
    plt.plot(h.history['loss'])
    plt.show()