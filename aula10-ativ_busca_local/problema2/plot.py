import math
import matplotlib.pyplot as plt

def fn(a):
    return a * math.sin(10*math.pi*a) + 1

if __name__ == "__main__":
    x = [i/1000 for i in range(-10000, 10000)]
    y = [fn(i) for i in x]

    plt.plot(x, y)
    plt.show()