from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BlogForm,CommentForm
from app.request import get_quote
from ..models import Blog,User,Comment
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db,photos
import markdown2 
@main.route("/pitches")
def posts(post_id):
    form = CommentForm()
    post = Pitch.query.get_or_404(post_id)
    comments = Comment.query.all()

    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, pitch_id=post.id )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts.post',post_id=post.id))
    return render_template('post.html', title = post.title, posts = posts,comments=comments, form=form)

@main.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_post():

    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content = form.content.data, category = form.category.data)
        db.session.add(blog)
        db.session.commit()
        
        return redirect(url_for('main.home'))
    return render_template('post.html',title = 'New Post', form = form, legend = 'New Post')

@main.route("/")
@main.route("/home")
def home():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Pitch app'

    
   page = request.args.get('page', 1, type=int)
   posts=Blog.query.all()
   quotes = get_quote()
   if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
   

   return render_template('home.html',posts=posts,quotes=quotes)

@main.route('/pitches/inspiration')
def inspiration():
    posts=Blog.query.filter_by(category='Inspirational')

    return render_template('inspirational.html', posts=posts)


@main.route('/pitches/biography')
def biograpghy():
    posts=Blog.query.filter_by(category='Biography')

    return render_template("biograghy.html", posts=posts)
main.route('/user/<uname>/pitches')
def user_pitches(uname):
   user = User.query.filter_by(username=uname).first()
   pitches = Pitch.query.filter_by(user_id=user.id).all()
 

   return render_template("profile/pitches.html", user=user, pitches=pitches, pitches_count=pitches_count, date=user_joined)

@main.route('/pitches/idea')
def idea():

   posts=Blog.query.filter_by(category='Ideas')

   return render_template("ideas.html", posts=posts)

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

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/comment')
def comment():
    form = CommentForm()
    posts = Comment.query.all()
    comment = Comment.query.all()

    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, pitch_id=blog.id )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.home',))
    return render_template('new_comment.html', title = post.title, posts = posts,comment=comment, comment_form=form,pitch_id=blog.id)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route("/post/<int:post_id>/update", methods= ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Pitch.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id =  post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title = 'Update Post', form = form, legend = 'Update Post')


@main.route("/post/delete", methods= ['GET','POST'])
@login_required
def delete_post(post_id):
    posts = Blog.query.all()
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
    