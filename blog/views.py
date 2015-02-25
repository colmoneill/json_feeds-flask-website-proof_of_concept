from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from blog.models import Post, Comment

posts = Blueprint('posts', __name__, template_folder='templates')

class ListView(MethodView):

	def get(self):
		posts = Post.objects.all()
		return render_template('posts/lists.html', posts=posts)

class DetailView(MethodView):

	def get(self, slug):
		post = Post.objects.get_or_404(slug=slug)
		return render_template('posts/detail.html', posts=posts)

#register the URLS
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))