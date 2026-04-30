import math
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def tanh(z):
    return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))

def relu(x):
    return max(0,x)

def plotSigmoid():
   
    x = np.linspace(-10, 10, 100)
    z = 1/(1 + np.exp(-x))

    plt.plot(x, z)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Sigmoid Activation Function')
    plt.grid(True)
    plt.show()

def plotRelu():
    x=np.linspace(-10,10,100)
    y=np.maximum(0, x)
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='ReLU', color='blue', linewidth=2)
    plt.title('ReLU Activation Function')
    plt.xlabel('Input (x)')
    plt.ylabel('Output f(x)')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    plt.show()


def plotTanh():
    x=np.linspace(-10,10,50)
    y=(np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    plt.plot(x, y, color = 'red', marker = "o")
    plt.title("numpy.tanh()")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

def main():
    plotTanh()
    plotSigmoid()
    plotRelu()

if __name__=="__main__":
    main()