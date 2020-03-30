import matplotlib.pyplot as plt
import numpy as np

def grafik_kuadrat(a, b, c):
    # 100 linearly spaced numbers
    x = np.linspace(-10, 10, 100)

    # the function, which is y = x^2 here
    y = a*x**2 + b*x + c

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title('Grafik Fungsi Metode Tabel')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x, y, 'r')

    # show the plot
    plt.show()