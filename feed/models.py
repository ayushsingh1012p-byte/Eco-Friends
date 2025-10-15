from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    eco_points = models.PositiveIntegerField(default=0) 
    rank = models.CharField(max_length=50, default='seedling')

    def __str__(self):
        return self.user.username
    
    def update_rank(self):
        if self.eco_points < 100:
            self.rank = 'seedling'
        elif self.eco_points < 500:
            self.rank = 'sprout'
        elif self.eco_points < 1000:
            self.rank = 'sapling'
        else:
            self.rank = 'tree'
        self.save()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def no_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name