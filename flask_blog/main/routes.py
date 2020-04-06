from flask import render_template, request, Blueprint
from flask_blog.models import Post

main = Blueprint('main', '__name__')


@main.context_processor
def inject_lastest_post_all_templates():
	latest_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
	return dict(latest_posts=latest_posts)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html',posts = posts)

@main.route('/about')
def about():
	return render_template('about.html', title = 'About')

