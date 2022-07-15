from django.db import models
from django.contrib.auth.models import User
from app.models import Food

class Order(models.Model):
    user = models.ForeignKey(User, related_name='Ulanyjy_sargyt', on_delete=models.CASCADE)
    order_status = [
            ("Nobatda", "Nobatda"),
            ("Ugradyldy", "Ugradyldy"),
            ("Tamamlandy", "Tamamlandy"),
            ("Yatyryldy", "Yatyryldy"), ]
    order_status = models.CharField(max_length=50, choices=order_status, default="Nobatda")
    payment = [
        ("Nagt", "Nagt"),
        ("Terminal", "Terminal"),]
    payment = models.CharField(max_length=15, choices=payment, default="Nagt")
    order_total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Zakaz'
        verbose_name_plural = 'Zakazlar'
    
    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, related_name='sargyt_naharlar', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    food_id = models.ForeignKey(Food, related_name='sargyt_edilen', on_delete=models.CASCADE)
    total = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Zakar Haryt'
        verbose_name_plural = 'Zakaz Harytlar'
    
    def __str__(self):
        return self.order_id.user.username
