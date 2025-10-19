import turtle
import random
import time
import math

# ---------------- Setup Screen ----------------
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle Fireworks Animation")
wn.setup(width=800, height=600)

# ---------------- Turtle Setup ----------------
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)
firework.penup()

# ---------------- Function to Draw One Firework ----------------
def draw_firework(x, y, color, particles=20, size=5, speed=10):
    for i in range(particles):
        angle = random.randint(0, 360)
        distance = random.randint(50, 150)
        rad = math.radians(angle)
        fx = x + distance * math.cos(rad)
        fy = y + distance * math.sin(rad)

        firework.goto(x, y)
        firework.pendown()
        firework.pencolor(color)
        firework.goto(fx, fy)
        firework.penup()

# ---------------- Random Fireworks Loop ----------------
colors = ["red", "yellow", "blue", "green", "orange", "purple", "cyan", "magenta"]

def animate_fireworks(times=10):
    for _ in range(times):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        color = random.choice(colors)
        particles = random.randint(15, 30)
        draw_firework(x, y, color, particles)
        time.sleep(0.5)
        firework.clear()

# ---------------- Run Animation ----------------
animate_fireworks(times=15)

# ---------------- End ----------------
turtle.done()
