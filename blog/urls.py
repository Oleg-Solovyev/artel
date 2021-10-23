from . import views
from django.urls import path
from django.urls import include

urlpatterns = [
    path('about/'      , views.about               , name='about'      ),
    path('blog/'       , views.PostList.as_view()  , name='blog'       ),
    path('en/'         , views.en                  , name='en'         ),
    path('upload/', views.image_upload_view),
    path(''            , views.home                , name='home'       ),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)