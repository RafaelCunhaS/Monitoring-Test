import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def generate_graph(data):
    transactions = pd.read_csv(data)
    x1, x2, y1, y2 = [], [], [], []
    x1.append(transactions['f0_'])
    print(x1)
    x2.append(transactions['f0_'][transactions['status'] != 'approved'])
    y1.append(transactions['f1_'])
    y2.append(transactions['f1_'][transactions['status'] != 'approved'])

    plt.cla()

    plt.plot(x1[0], y1[0], label='Approved')
    plt.plot(x2[0], y2[0], label='Not Approved')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), generate_graph, interval=1000)

plt.tight_layout()
plt.show()
