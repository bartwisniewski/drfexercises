from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Basket(models.Model):
    timestamp = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.name:
            self.name = f"dummy"
            super().save(force_insert, force_update, using, update_fields)
            self.name = f"customer{self.pk}"
        super().save(force_insert, force_update, using, update_fields)


@receiver(post_save, sender='customers.Customer')
def customer_post_save(sender, instance, created, **kwargs):
    if created:
        basket = Basket()
        basket.save()
        instance.basket = basket
        instance.save()
