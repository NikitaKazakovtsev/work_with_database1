from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(max_length=255)
    lte_exists = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)
    
    def __str__(self):
        return self.name