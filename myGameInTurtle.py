import turtle

##### python myGameInTurtle.py #####

# Crear una ventana de turtle
window = turtle.Screen()
window.title("Mi Juego")

# Crear un personaje
player = turtle.Turtle()
player.shape("square")
player.color("black")

# Función para mover el personaje
def move_player(x, y):
    player.goto(player.xcor() + x, player.ycor() + y)

# Asignar teclas a funciones
window.listen()
window.onkeypress(lambda: move_player(-10, 0), "a")
window.onkeypress(lambda: move_player(10, 0), "d")
window.onkeypress(lambda: move_player(0, 10), "w")
window.onkeypress(lambda: move_player(0, -10), "s")

# Bucle principal
turtle.mainloop()