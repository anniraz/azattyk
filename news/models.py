from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=140,db_index=True)
    url=models.SlugField(null=True,unique=True,db_index=True,verbose_name='URL')  
      
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category',kwargs={'categ_id':self.pk})

    class Meta:
        verbose_name_plural = "Категории"

    
class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    description = models.TextField()
    url=models.SlugField(null=True,unique=True,db_index=True,verbose_name='URL')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.url})

    class Meta:
        verbose_name_plural = "Новости"
    
