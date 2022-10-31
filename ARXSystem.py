import math
from collections import deque

global Y, A, B, d, T, m, p, k

Y = [0, 0, 0, 0, 0]

#Variables should be read from a txt file
A = [0, 0, 0, 0, 0]
B = [0, 0, 0, 0, 0, 0]
d = 0
#Intervalo de muestreo
T = 0

#Entrada escalón - Input - can be changed at any moment
m = []
p = 0
k = 0

def rotate(l, n):
    return l[n:] + l[:n]

def readFiles():
    global m
    with open(input("Please enter txt file name for 'm': "), 'r') as f:
        for value in f:
            m.append(float(value))
    f.close()


def readVar():
    global d, p, T, A, B
    print("Please input 5 values for a.")
    for i in range(len(A)):
        A[i] = float(input("Value " + str(i) + " : "))

    print("\nPlease input 5 values for b.")
    for i in range(len(B)):
        B[i] = float(input("Value " + str(i) + " : "))

    print("\nPlease input value for d.")
    d = float(input("Value: "))

    print("\nPlease input value for p.")
    p = float(input("Value: "))

    print("\nPlease input value for Time Intervals.")
    T = float(input("Value: "))



def calculateOutput(k):
    global Y, A, B, d, p
    ValueA = A[0]*Y[0] + A[1]*Y[1] + A[2]*Y[2] + A[3]*Y[3] + A[4]*Y[4]
    ValueB =  B[0]*calculateBInputs(k-d) + B[1]*calculateBInputs(k-d-1) + B[2]*calculateBInputs(k-d-2) + B[3]*calculateBInputs(k-d-3) + B[4]*calculateBInputs(k-d-4) + B[5]*calculateBInputs(k-d-5) + p
    print(ValueA)
    print(ValueB)
    lastY = ValueA+ValueB
    k=k+1
    rotate(Y, -1)
    Y[0] = lastY
    return lastY

def calculateBInputs(k):
    if(k < 0):
        return 0   
    return m[int(k)]

    
    
readFiles()
readVar()
for i in range(15):
    hi = calculateOutput(k)
    print("Round " + str(i) +": " + str(hi))