from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


class MyUser(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    display_name = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class LoginHistory(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True)
    successful = models.BooleanField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        successful_string = "login successful" if self.successful else "login failed"
        ip_string = f" from {self.ip}" if self.ip else ""
        return f"tried to login as {self.user.username}, {successful_string}{ip_string}"

    def __str__(self):
        successful_string = "login successful" if self.successful else "login failed"
        ip_string = f" from {self.ip}" if self.ip else ""
        return f"tried to login as {self.user.username}, {successful_string}{ip_string}"


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    LoginHistory.objects.create(successful=True, ip=ip, user=user)


@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    username = credentials.get('username', None)
    try:
        user = MyUser.objects.get(username=username)
        LoginHistory.objects.create(successful=False, ip=None, user=user)
    except MyUser.DoesNotExist:
        pass
