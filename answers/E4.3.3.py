import turtle


def polygon(t, n):
    for i in range(n):
        t.fd(100)
        t.lt(360.0/n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    polygon(bob, 5)
    turtle.mainloop()
