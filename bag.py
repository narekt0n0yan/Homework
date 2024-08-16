

volume = [1,2,3,4,5]
value = [12,16,18,20,22]

def bag(x: list, y: list, V: float):
    x.sort()
    x.reverse()    
    y.sort()
    y.reverse()

    result:float = 0


    for i in range(len(x)):
        if V - y[i] > 0:
            V = V - y[i]
            result = result + x[i]
            print(y[i])

        else:
            result = result + (x[i]/y[i]) * V
            print(V)
            break
    print(result)

bag(value, volume, 13)


def bag1(x,y,V):
    