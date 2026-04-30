import math


def singleneuron(x1, x2, w1, w2, bias):
    z=0
    z= (x1*w1+x2*w2)+bias

    return z

def Sigmoid(z):
    Sigmoid=1 / (1 + math.exp(-z))

    return Sigmoid

def main():
    x1=2
    x2=3
    w1=0.4
    w2=0.6
    bias=0.5
    z=singleneuron(x1, x2, w1, w2, bias)

    Output=Sigmoid(z)

    print("final output is : ", Output)

    if (Output>=0 and Output<0.5):
        print("Output is close to zero")
    elif(Output>=0.5 and Output<=1):
        print("Output is close to one")



if __name__=="__main__":
    main()