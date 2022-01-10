import turtle

def main():
    # create a turtle object
    michaelangelo = turtle.Turtle()
    michaelangelo.color((150,90,90))
    # ask the turtle to move around the canvas
    for i in range(4):
        michaelangelo.forward(50)
        michaelangelo.right(90)
if __name__ == "__main__":
    main()