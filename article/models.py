from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name='Categorie'

    def __str__(self):
        return self.name
    


class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    category=models.ForeignKey(Category ,on_delete = models.CASCADE,default=1)
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=8000)
    image=models.ImageField(upload_to='article_images/',default="img.jpg")   ## if we use the image fileds then we set the path for this images to store in one seprate folder(thats we set a path ib settings.py  Static path (media_urls and Media_root))
    pub_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('profile')
    

class WatchlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,default=None)
    pub_date=models.DateField(auto_now=True)
    class Meta:
        unique_together=['user','article']


class Comment(models.Model):
    comment=models.TextField(max_length=8000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    hold=models.ForeignKey('self',on_delete=models.CASCADE ,null=True,related_name='+')
    pub_date=models.DateField(auto_now=True)
