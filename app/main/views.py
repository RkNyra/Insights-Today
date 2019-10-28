from flask import render_template, request,redirect,url_for,abort
from . import main
from ..models import User
from .forms import SharePostForm, UpdateProfile
from ..import db
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

# user profile page
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# update profile page
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)