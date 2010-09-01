#coding: utf-8
from flask import Flask
app = Flask(__name__)
app.debug = True

from google.appengine.ext import db

from flask import redirect, url_for, request, render_template, abort, flash, get_flashed_messages
import tweepy
import random

CONSUMER_KEY = 'your own consumer key'
CONSUMER_SECRET = 'your own consumer secret'
TOKEN_KEY = 'token key'
TOKEN_SECRET = 'token secret'

class Contexts(db.Model):
    context = db.StringProperty()

@app.route('/post_form/')
def post_form(context=None):
    return render_template('form.html')

@app.route('/post_update/',methods=['GET','POST'])
def post_update():
    if request.method == 'POST':
        context = request.form['context']
        update(context)
        return redirect(url_for('post_form'))
    return 'Sample'

@app.route('/rnd_update/')
def rnd_update():
    query = Contexts.all()
    results = query.fetch(1000)
    result = results[random.randint(len(results)-1,0)]
    update(result.context)
    return None
    
@app.route('/insert_form/',methods=['GET','POST'])
def insert_form(context = None):
    if request.method == 'POST':
        context_str = request.form['context']
        cont = Contexts(context=context_str)
        db.put(cont)
    else:
        pass
    return render_template('insert_form.html')

    

@app.route('/update/')
def update(context = None):
    if context != None:
        context = context.encode('utf-8')
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(TOKEN_KEY,TOKEN_SECRET)
        api = tweepy.API(auth)
        api.update_status(context)

# set the secret key.  keep this really secret:

if __name__ == '__main__':
    app.run()
