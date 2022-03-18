#! /usr/bin/python3
t = 0
def helloworld():
    for a in range(1,101):
        if a%2 ==0:
            print(str(a) +"--even")
        else:
            print(str(a) +"--odd")
    print("Hello World improved!")

helloworld()
