from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("load_posts/", views.load_posts, name="load_posts"), 
    path("group_load_posts/", views.group_load_posts, name="group_load_posts"), 
    path("terms", views.terms, name="terms"),
    path("newpost", views.newPost, name="newPost"),
    path('groups/create/', views.create_group, name='create_group'),
    path('groups/<int:group_id>/join/', views.join_group, name='join_group'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('group_post/<int:group_id>/', views.group_newPost, name='group_newPost'),
    path('group_addComment/<int:post_id>/', views.group_addComment, name='group_addComment'),
    path('my_groups/', views.my_groups_view, name='my_groups'),
    path('joined_groups/', views.joined_groups_view, name='joined_groups'),
    path('group/<int:group_id>/delete/', views.delete_group_view, name='delete_group'),
    path('search/', views.search, name='search'),
    path('group/<int:group_id>/exit/', views.exit_group_view, name='exit_group'),
    path("post_content/<int:post_id>", views.post_content, name="post_content"),
    path("group_post_content/<int:post_id>", views.group_post_content, name="group_post_content"),
    path("post_image/<int:post_id>", views.post_image, name="post_image"),
    path('profile_pic/<int:user_id/', views.profile_pic, name="profile_pic"),
    path('profile/<int:user_id>/', views.profile, name="profile"),
    path('edit_profile/<int:user_id>/', views.edit_profile, name="edit_profile"),
    path('addComment/<int:post_id>/', views.addComment, name='addComment'),
    path("follow", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("following", views.following, name="following"),
    path("like_count", views.like_count, name="like_count"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("remove_like/<int:post_id>", views.remove_like, name="remove_like"),
    path("add_like/<int:post_id>", views.add_like, name="add_like"),
    path("remove_shock/<int:post_id>", views.remove_shock, name="remove_shock"),
    path("add_shock/<int:post_id>", views.add_shock, name="add_shock"),
    path("remove_love/<int:post_id>", views.remove_love, name="remove_love"),
    path("add_love/<int:post_id>", views.add_love, name="add_love"),
    path("remove_haha/<int:post_id>", views.remove_haha, name="remove_haha"),
    path("add_haha/<int:post_id>", views.add_haha, name="add_haha"),
    path("remove_sad/<int:post_id>", views.remove_sad, name="remove_sad"),
    path("add_sad/<int:post_id>", views.add_sad, name="add_sad"),
    path("group_add_or_remove_reaction/<int:post_id>/<str:reaction_type>/", views.group_add_or_remove_reaction, name="group_add_or_remove_reaction"),
    path("general_library", views.general_library, name="general_library"),
    path("my_library", views.my_library, name="my_library"),
    path("view_video/<int:video_id>/", views.view_video, name="view_video"),
    path("view_document/<int:document_id>/", views.view_document, name="view_document"),
    path("upload_document/", views.upload_document, name="upload_document"),
    path("upload_video/", views.upload_video, name="upload_video"),
    path('category/<str:category_name>/', views.category_detail, name='category_detail'),
    path('add_to_favorites/<int:item_id>/<str:item_type>/', views.add_to_favorites, name='add_to_favorites'),
    path('forum/', views.forum, name='forum'),
    path('forum/create_topic/', views.create_topic, name='create_topic'),
    path('forum/topic/<int:topic_id>/', views.view_topic, name='view_topic'),
    path('forum/topic/<int:topic_id>/add_post/', views.add_forum_post, name='add_forum_post'),
    path('new_announcement', views.new_announcement, name="new_announcement"),
    path("announcements", views.announcements, name="announcements"),
    path('all_groups/', views.all_groups, name='all_groups'),
    path("login", views.login_view, name="network_login"),
    path("logout", views.logout_view, name="network_logout"),
    path("register", views.register, name="network_register"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),



]
