from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog import sitemaps
from blog.sitemaps import PostSitemap
from blog.feeds import LatestPostsFeed
sitemaps = {'posts':PostSitemap, }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap' ),
    path('feed/', LatestPostsFeed(), name='latest_posts_feed'),
]
