from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    categ = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.categ}'

class AdvertiseSell(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(default='default_prod.jpeg', upload_to='product_images')
    price = models.CharField(max_length=10, default='XXXX')
    negotiable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} | {self.author.username}'

    def get_absolute_url(self):
        return reverse('sell_detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        super().save()

        product_image = Image.open(self.product_image.path)

        if product_image.height > 300 or product_image.width > 300:
            output_size = (300, 300)
            product_image.thumbnail(output_size)
            product_image.save(self.product_image.path)

        try:
            this = Profile.objects.get(id=self.id)
            if this.product_image != self.product_image:
                this.product_image.delete()
        except: pass

class AdvertiseBuy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.CharField(max_length=10, default='XXXX')
    negotiable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} | {self.author.username}'

    def get_absolute_url(self):
        return reverse('buy_detail', args=[str(self.pk)])
