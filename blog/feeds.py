from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
	title = 'SGB'
	link = '/blog/'
	description = 'New posts'

	def items(self):
		return Post.published.all()[:5]
	def item_title(self, obj):
		return obj.title
	def item_description(self, obj):
		return truncatewords(obj.body, 30)