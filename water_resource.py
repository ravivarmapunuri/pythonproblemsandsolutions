import numpy as np 

def find_widest_valley(n, A ,B):
    x= np.linspace(0,2**np.pi, num=1000)
    y= np.zeros_like(x)

    for i in range(n):
        y += A[i] *np.sin((i+1) * x + B[i])

    peaks=np.where((np.diff(np.sign(np.diff(y))))  == -2)[0]

    max_width = 0
    widest_valley = 0


    for i in range(len(peaks) - 1):
        width = x[peaks[i+1]] - x[peaks[i]]
        if width> max_width:
            max_width = width
            widest_valley = i+1
    
    return widest_valley + 1


n1 = int(input())
A1 = list(map(int,input().split()))[n1:]
B1 = list(map(int,input().split()))[n1:]

output1 = find_widest_valley(n1,A1,B1)
print(output1)