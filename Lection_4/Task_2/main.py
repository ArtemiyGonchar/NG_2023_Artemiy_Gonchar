from flask import Flask, render_template, request
import random

server = Flask("Walking @")

tableSize = 5
#RANDOM START POSITION FOR FIRST ENTERING ON PAGE
y = random.randrange(0, tableSize)
x = random.randrange(0, tableSize)

tableForWalk = ['.'] * tableSize

for dotFilling in range(tableSize):
    tableForWalk[dotFilling] = ['.'] * tableSize

tableForWalk[y][x] = "@"

for i in tableForWalk:
    print(i)

@server.route('/', methods = ["GET", "POST"])
def index():
    global x
    global y
    action = request.args.get('action')
    if action != '':
        match action:
            case "up":
                tableForWalk[y][x] = '.'
                y -= 1
            case "down":
                tableForWalk[y][x] = "."
                y += 1
            case "right":
                tableForWalk[y][x] = "."
                x += 1
            case "left":
                tableForWalk[y][x] = "."
                x -= 1
        if y < 0:
            y = 0
        elif y > tableSize - 1:
            y = tableSize - 1
        if x > tableSize - 1:
            x = tableSize - 1
        elif x < 0:
            x = 0
        tableForWalk[y][x] = '@'
    return render_template('index.html', table = tableForWalk)

    

server.run(host='0.0.0.0', port=8080)