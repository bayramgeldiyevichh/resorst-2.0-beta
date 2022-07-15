from django.db import models
from django.contrib.auth.models import User


class Restoran(models.Model):
    STATE = (("Mary", "Mary"),
            ("Ahal", "Ahal"),
            ("Balkan", "Balkan"),
            ("Lebap", "Lebap"),
            ("Daşoguz", "Daşoguz"),
            ("Aşgabat", "Aşgabat"),)
    name = models.CharField(max_length=120, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_vip = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="products")
    banner_img = models.ImageField(upload_to="products")
    region = models.CharField(max_length=50, choices=STATE, default="Mary")
    address_line = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=64, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    instagram = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Restoran'
        verbose_name_plural = 'Restoranlar'
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    state_region = models.CharField(max_length=35)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='category', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
    
    def __str__(self):
        return self.name



class Food(models.Model):
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    food_image = models.ImageField(upload_to="products")
    food_cat = models.ForeignKey(Category, related_name='cat_food', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Nahar'
        verbose_name_plural = 'Naharlar'
    
    def __str__(self):
        return self.name



class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Nahar_surat'
        verbose_name_plural = 'Nahar_suratlar'
    
    def __str__(self):
        return self.food.name


class Olceg(models.Model):
    title = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ölçegler'
        verbose_name_plural = 'Ölçegler'
    
    def __str__(self):
        return self.title
    

class Sostav(models.Model):
    olceg = models.ForeignKey(Olceg, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=120)
    quantity = models.FloatField()
    food_id = models.ForeignKey(Food, related_name='Nahar', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Düzümi'
        verbose_name_plural = 'Düzümi'
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kommentariya"
        verbose_name_plural = "Kommentariyalar"

    def __str__(self):
        return self.user.username

class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="banners/")
    url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Bannerlar"
    
    def __str__(self):
        return self.title

