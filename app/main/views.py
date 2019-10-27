from flask import render_template

from . import main


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

    '''
    View share post page function that returns the post sharing page and its data
    '''
    
    title = 'Insights Today'
    return render_template('sharepost.html', title=title)