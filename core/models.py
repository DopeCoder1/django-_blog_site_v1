from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="URL", db_index=True, unique=True, max_length=100)
    content = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создание")
    time_update = models.DateTimeField(auto_now=True, verbose_name="дата изменение")
    is_published = models.BooleanField(verbose_name="Опубликован ли?")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=100, verbose_name="URL", unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})
