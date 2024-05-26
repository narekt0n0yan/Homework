from random import randint
X = [[1,2],
     [5,6],
     [6,4],
     [8,6],
     [3,5],
     [9,6],
     [12,6],
     [10,9],
     [6,3],
     [9,3]]

Y = [0,0,0,0,0,
     1,1,1,1,1]

 

def line(x, k, b) -> float:
    return k * x + b


def calc_RSS(X, k, b) -> float:
    RSS = 0
    for i in X:
        RSS += (i[1] - line(i[0], k, b)) ** 2
    return RSS

def grad_RSS(X, k, b):
    grad_k = 0
    grad_b = 0
    for i in X:
        grad_k += (2 * i[1] * i[0]) + (2 * k * i[0] ** 2) + (2 * i[0] * b)
        grad_b += (-2 * i[1]) + (2 * k * i[0]) + (2 * b) 
    return grad_b, grad_k

print(calc_RSS (X, 0.5, 1))
print(grad_RSS(X , randint(1,10), randint(1,10)))


    