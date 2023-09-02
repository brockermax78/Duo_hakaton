from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
        
        
class Games(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=30, blank=True, primary_key=True)
    description = models.TextField()
    image = models.ImageField(upload_to='games', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.title}->{self.description}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
        
