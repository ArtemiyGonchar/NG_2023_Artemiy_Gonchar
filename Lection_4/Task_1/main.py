from flask import Flask, render_template, request

server = Flask("Calculator")

@server.route('/')
def index():
    return render_template("index.html")

@server.route('/result')
def result():
    valueA = float(request.args.get("valueA"))
    valueB = float(request.args.get("valueB"))
    action = str(request.args.get("action"))
    result = None
    match action:
        case "*":
            result = str(valueA*valueB)
        case "/":
            result = str(valueA/valueB)
        case "+":
            result = str(valueA+valueB)
        case "-":
            result = str(valueA-valueB)
        case "**":
            result = str(valueA**valueB)
        case "square roots":
            return "Result A :"+str(valueA ** 0.5)+" "+"Result B: "+str(valueB** 0.5)
    return "Result: "+result

server.run(host="0.0.0.0", port=8080)