from django.urls import path
from . import views
urlpatterns = [
    path("", views.blog_title),# "" 表示访问根目录，在blog 中代表 根目录/blog/
    path("<int:article_id>/", views.blog_article),

]