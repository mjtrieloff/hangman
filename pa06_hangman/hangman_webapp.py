"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':"interesting",
         'word_so_far':"-----------",
         'done':False,
         'tries':[]}

@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')

@app.route('/start')
def play():
    global state
    state['word']=hangman_app.generate_random_word()
    state['guesses'] = []
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return play()
    elif request.method == 'POST':
        letter = request.form['guess']
        state['tries'] == 0
        score = []
        word = state['word']
        word_so_far = len(state['word']) * "_"
        state['word_so_far'] = list(word_so_far)
        letter = request.form['guess']
        if letter in state['guesses']:
            return "You already guessed that word. Go back and guess again"
            state['tries'] += [letter]
        elif letter in state['word']:
            index = state['word'].index(letter)
            state["word_so_far"][index] = letter
            score += [letter]
        elif letter not in state['word']:
            state['guesses'] += [letter]
            state['tries'] += [letter]
        if len(score) == len(state['word']):
            return "You guessed the word:"+state['word']
        if len(state['tries']) == 6:
            return "You Lose!"
    return render_template('play.html',state=state)


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
