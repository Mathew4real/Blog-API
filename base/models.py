from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django .conf import settings
from django.utils.text import slugify
from django .utils import timezone


class User(AbstractUser):
    bio = models.CharField(max_length=300,blank=True,null= True)
    profile_pic = models.ImageField(upload_to="profile_img",blank = True,null = True)
    facebook = models.URLField(max_length=255,blank=True,null=True)
    linkedin = models.URLField(max_length=255,blank=True,null=True)
    instagram = models.URLField(max_length=255,blank=True,null=True)
    github = models.URLField(max_length=255,blank=True,null=True)
    youtube = models.URLField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.username
    

class Category(models.TextChoices):
        TECHNOLOGY = 'technology', 'Tecnologia'
        DEVELOPMENT = 'development', 'Desenvolvimento'
        AI = 'ai', 'Inteligência Artificial'
        SCIENCE = 'science', 'Ciência'
        EDUCATION = 'education', 'Educação'
        TUTORIALS = 'tutorials', 'Tutoriais'
        PRODUCTIVITY = 'productivity', 'Produtividade'
        GAMING = 'gaming', 'Games'
        MOVIES = 'movies', 'Filmes e Séries'
        BOOKS = 'books', 'Livros'
        HEALTH = 'health', 'Saúde'
        TRAVEL = 'travel', 'Viagens'
        FINANCE = 'finance', 'Finanças'
        ENTREPRENEURSHIP = 'entrepreneurship', 'Empreendedorismo'
        NEWS = 'news', 'Notícias'
        OPINION = 'opinion', 'Opinião'

class Blog(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,related_name="blogs",null=True)
        slug = models.SlugField(max_length=255,unique=True,blank=True)
        created = models.DateTimeField(auto_now_add=True)
        update = models.DateTimeField(auto_now=True)
        is_draft = models.BooleanField(default=True)
        category = models.CharField(max_length=50,choices=Category.choices)
        image = models.ImageField(upload_to="blog_img",blank=True,null=True) 

        class Meta:
              ordering = ["-created"]
        
        def __str__(self):
              return self.title
        
        def save(self,*args,**kwargs):
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Blog.objects.filter(slug = slug).exists():
                slug = f"{base_slug}-{num}"
                num +=1
            self.slug = slug

            if not self.is_draft and self.created is None:
                self.created = timezone.now()
            super().save(*args, **kwargs) 
              

