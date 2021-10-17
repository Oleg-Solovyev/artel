from . import views
from django.urls import path

urlpatterns = [
    path('about/'      , views.about               , name='about'      ),
    path('blog/'       , views.PostList.as_view()  , name='blog'       ),
    path('en/'         , views.en                  , name='en'         ),
    path(''            , views.home                , name='home'       ),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
