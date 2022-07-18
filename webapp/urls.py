from django.urls import path
from .views import ArticleDetail, ArticleList

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleList.as_view()),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    # path('detail/<int:id>', article_detail),
]
