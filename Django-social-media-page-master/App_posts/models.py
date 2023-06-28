from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='post' )
    image=models.ImageField(upload_to='post_images')
    caption=models.CharField(max_length=264,blank=True)
    upload_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-update_time']


class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='Liked_post')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.user,self.post)
