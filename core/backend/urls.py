from django.urls import path
# from .views import article_list, article_details
from .views import ArticleList, ArticleDetails


urlpatterns = [
    # path('', article_list),
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details),

    path('articles/', ArticleList.as_view()),
    path('articles/<slug:slug>/', ArticleDetails.as_view()),
]
