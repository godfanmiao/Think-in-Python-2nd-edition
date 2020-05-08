import turtle


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)


if __name__ == "__main__":
    bob = turtle.Turtle()
    square(bob, 200)
    turtle.mainloop()