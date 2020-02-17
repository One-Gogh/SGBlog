from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag()# == @register.simple_teg(name='total_posts')
def get_total_posts():
	return Post.published.count()

@register.inclusion_tag('blog_temp/post_temp/latest_posts.html')
def get_latest_posts(count=5):
	latest_posts = Post.published.order_by('-publish')[:count]
	return {"latest_posts":latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
	return Post.published.annotate(total_comment=Count('comment')).order_by('-total_comment')[:count]

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))