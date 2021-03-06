from django.db import models

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class PublishingHouse(models.Model):
    pub_name = models.TextField()
    def __str__(self):
        return self.pub_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="autor_books")
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField( default=0, max_digits=19, decimal_places=2)
    pub = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, related_name="pub_books", null=True)
    def __str__(self):
        return self.title
# Create your models here.

