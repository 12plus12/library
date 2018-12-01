from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'tb_books'