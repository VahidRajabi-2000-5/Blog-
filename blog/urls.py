from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="posts_list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("create/",views.PostCreateView.as_view(),name='post_create'),
    path("<int:pk>/update/",views.PostUpdateView.as_view(),name='post_update'),
    path("<int:pk>/delete/",views.PostDeleteView.as_view(),name='post_delete'),
    # path("", views.posts_list_view, name="posts_list"),
    # path("<int:pk>/", views.post_detail_view, name="post_detail"),
    # path("create/",views.post_create_view,name='po/st_create'),
    # path("<int:pk>/update/",views.PostUpdateView.as_view(),name='post_update'),
    # path("<int:pk>/delete/",views.PostDeleteView.as_view(),name='post_delete'),
]
