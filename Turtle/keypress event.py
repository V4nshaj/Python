from turtle import *
import turtle
turtle.setup(400,500,10,20)    # Determine the window size
wn = turtle.Screen()     # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen") # Set the background color
tess = turtle.Turtle()   # Create our favorite turtle
# The next four functions are our "event handlers".
def h1():
   tess.forward(30)
def h2():
   tess.backward(30)
def h3():
   tess.left(45)
def h4():
   tess.right(45)
def h5():
    wn.bye()      # Close down the turtle window
# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Down")
wn.onkey(h3, "Left")
wn.onkey(h4, "Right")
wn.onkey(h5, "q")
# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
