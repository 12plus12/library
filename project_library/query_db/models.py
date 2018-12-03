from django.db import models

# Create your models here.


class AuthorInfo(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_authors'


class BookInfo(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(AuthorInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_books'