from flask import Flask, render_template, request, redirect
import random 	                # import the random module
app = Flask(__name__)


randomNumber = random.randint(1, 100)
attempts = 0

@app.route('/')
def guess_num():
    global randomNumber
    global attempts
    print( randomNumber )
    return render_template( "guess.html", randomNumber = randomNumber, attempts = attempts )

@app.route('/low')
def too_low():
    global randomNumber
    global attempts
    return render_template( "low.html", randomNumber = randomNumber, attempts = attempts )

@app.route('/high')
def too_high():
    global randomNumber
    global attempts
    return render_template( "high.html", randomNumber = randomNumber, attempts = attempts )

@app.route('/correct')
def correct_answer():
    global randomNumber
    global attempts
    print( randomNumber )
    return render_template( "correct.html", randomNumber = randomNumber, attempts = attempts )

@app.route('/guess', methods = ['POST'])
def check_answer():
    global randomNumber
    global attempts
    attempts += 1
    guess = int( request.form["guess"] )
    if guess < randomNumber:
        return redirect( '/low' )
    if guess > randomNumber:
        return redirect( '/high' )
    if guess == randomNumber:
        return redirect( '/correct' )

@app.route('/play_again', methods = ['POST'])
def play_again():
    global randomNumber
    global attempts
    randomNumber = random.randint(1, 100)
    attempts = 0
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)