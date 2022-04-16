from turtle import*
n=int(input("input number of edge: "))
x=360/n
for i in range (n+1):
    forward(50)
    left(x)
mainloop()