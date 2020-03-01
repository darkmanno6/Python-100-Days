import turtle


# 画一个正方形；
def paint():
    turtle.pensize(10)
    turtle.pencolor('red')
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.mainloop()


if __name__ == "__main__":
    paint()
