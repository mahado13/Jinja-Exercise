from cProfile import label
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

'''
Author: Mahad Osman
Date: Nov 15, 2022
Exercise: Jinja Exercise 
'''
app = Flask(__name__)

'''Tool bar Debug setup'''
app.config['SECRET_KEY'] = "not-so-secret" 
debug =DebugToolbarExtension(app)


@app.route('/')
def show_home():
    '''Our simple home page'''
    return "<H1>Welcome Home</H1>"

@app.route('/form')
def show_form():
    ''' Our form Page setup to render the prompts 
        - Labels will be set to the prompts of our story object

    '''
    labels = story.prompts
    return render_template("form.html", labels = labels)

@app.route('/stories')
def show_stories():
    ''' Our stories page which will generate our sentence
        information will use story.generate function with our provided information
        Returns our rendered html template with the new sentence
    '''
    information  = story.generate(request.args)
    return render_template("stories.html", information = information)