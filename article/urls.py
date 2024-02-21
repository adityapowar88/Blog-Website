from django.urls import path
from .views import *

app_name='article'


urlpatterns = [
    path('',index,name='index'),
    path('article/search/',serach_article,name='serach'),
    path('article/<int:pk>/',single_article,name='single_article'),
    path('article/category/<int:pk>',categorised_articles,name='categorised_articles'),
    path('article/post/', post_article, name= 'post_article'),
    path('article/update/<int:pk>',update_article.as_view(), name='update_article'),
    path('article/delete/<int:pk>/',DeleteArticle.as_view(), name="delete_article"), 

    path('watchlist/',watchlist, name='watchlist'),
    path('addWatchlist/',add_watchlist, name='add_watchlist'),
    path('remove/<int:pk>/',remove_watchlist, name='remove_watchlist'),

]

