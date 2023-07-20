from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="post_user")
    postContent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='post_image/', null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.postContent} {self.timestamp}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userComment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="postComment")
    message = models.CharField(max_length=10000)

    def __str__(self):
        return f"{str(self.author)} commented on {self.post}"
    
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="following_user")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="followed_user")

    def __str__(self):
        return f"{self.following} is following {self.follower}"

# Regular post reactions
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")

    def __str__(self):
        return f"{self.user} likes {self.post}"

class Sad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userSad")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postSad")

    def __str__(self):
        return f"{self.user} reacts Sad on {self.post}"

class Love(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userLove")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postLove")

    def __str__(self):
        return f"{self.user} reacts Love on {self.post}"

class Haha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userHaha")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postHaha")

    def __str__(self):
        return f"{self.user} reacts Haha on {self.post}"

class Shock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userShock")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postShock")

    def __str__(self):
        return f"{self.user} reacts Shock on {self.post}"

# Define the Group model and GroupPost model
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='group_members')

    def __str__(self):
        return f"{self.name}"

class GroupPost(Post):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_posts")

class GroupComment(Comment):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_comments")

# Group post reactions
class GroupLike(Like):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="group_post_likes")

class GroupSad(Sad):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="group_post_sads")

class GroupLove(Love):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="group_post_loves")

class GroupHaha(Haha):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="group_post_hahas")

class GroupShock(Shock):
    group_post = models.ForeignKey(GroupPost, on_delete=models.CASCADE, related_name="group_post_shocks")
