from flask import render_template, request,redirect,url_for
from . import main
from .forms import SharePostForm
from flask_login import login_required


#Views

# home page
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Insights Today'
    return render_template('index.html', title=title)

# sharepost page
@main.route('/sharepost')
def sharepost():
    
    form = SharePostForm()

    '''
    View share post page function that returns the post sharing page and its data
    '''
    
    title = 'Insights Today'
    return render_template('sharepost.html', title=title, SharePostForm=form)