import turtle


def square(t):
    for i in range(4):
        t.fd(100)
        t.rt(90)


if __name__ == '__main__':
    bob = turtle.Turtle()
    square(bob)
    turtle.mainloop()
