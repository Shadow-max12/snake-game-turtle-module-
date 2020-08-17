import turtle
import time
import random
 
score = 0
high_score = 0
x = 0
y = 0
count = 0

# Screen setup 
win = turtle.Screen()
win.title("My snake game")
win.bgcolor("cyan")
win.setup(width = 600, height = 600)
win.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(x,y)
head.direction = "stop"

#food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(x,y+30)

#score
sc = turtle.Turtle()
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score = 0     High Score = 0",False,align = "center",font=("Times New Roman Baltic",20,"normal"))

#drawing a line below score board
pen = turtle.Turtle()
pen.penup()
pen.goto(-290,255)
pen.pendown()
pen.forward(580)
pen.hideturtle()

#funcions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "right":
            head.setx(head.xcor()+ 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
            
def deletebody():
    for i in range(0,len(segment)):
        segment[i].hideturtle()

        
# setting keyboard button
win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")

segment = []
        
# main game loop
while True:
    win.update()
    
    #checking border collision
    if head.xcor() > 290 or head.xcor() < -295 or head.ycor() > 235 or head.ycor() < -280:
        head.direction = "stop"
        time.sleep(1)
        deletebody()
        segment.clear()
        head.goto(0,0)
        food.goto(0,30)
        head.write("Game over!!",False,align = "center",font=("Times New Roman Baltic",25,"bold"))
        time.sleep(1) 
        head.clear()
        score = 0
        sc.clear()
        sc.write("Score = {}     High score = {}".format(score, high_score),False,align = "center",font = ("Times New Roman Baltic",20,"normal"))

    # Detecting food eat  
    if head.distance(food) < 20:
        count+=1
        x = random.randint(-292,290)
        y = random.randint(-292,260)
        food.goto(x,y)
        # Adding score
        sc.reset()
        sc.penup()
        sc.goto(0,270)
        sc.hideturtle()
        score+=10
        if score >= high_score:
            high_score = score
        sc.write("Score = {}     High score = {}".format(score, high_score),False,align = "center",font = ("Times New Roman Baltic",20,"normal"))
       
        if count == 2:
            #segment
            body = turtle.Turtle()
            body.speed(0)
            body.shape("square")
            body.color("grey")
            body.penup()
            segment.append(body)
            count = 0
                       
    
        
    #body segmnets movement
    for i in range((len(segment) -1),0,-1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x,y)
       
    #moving segment near head to head position        
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()    

    # checkingbody collision
    for s in segment:
        if s.distance(head) < 20:
            head.direction = "stop"
            time.sleep(1)
            deletebody()
            segment.clear()
            head.goto(0,0)
            food.goto(0,30)
            head.write("Game over!!",False,align = "center",font=("Times New Roman Baltic",25,"normal"))
            time.sleep(1) 
            head.clear()
            score = 0
            sc.clear()
            sc.write("Score = {}     High score = {}".format(score, high_score),False,align = "center",font = ("Times New Roman Baltic",20,"normal"))

   
            
 
    time.sleep(0.070)

win.mainloop()
