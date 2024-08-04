from django.db import models

# Create your models here.

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.name()


class Tag(models.Model):
    tag=models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Post(models.Model):
    title=models.CharField(max_length=50)
    tag=models.ManyToManyField(Tag)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photos', height_field=None, width_field=None, max_length=None)
    date=models.DateField(auto_now=False, auto_now_add=False)
    content=models.TextField()
    slug=models.SlugField()

    def __str__(self):
        return self.title
    

class Contact(models.Model):
        name=models.CharField(max_length=50)
        mail=models.EmailField(max_length=254)
        message=models.TextField()

