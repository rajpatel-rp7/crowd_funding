from django.db import models
from django.conf import settings
from django.conf import settings as django_settings
import os


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d')
    twitter = models.TextField(null=True)
    profession = models.TextField(null=True)
    persional_detail = models.TextField(null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def get_picture(self):
        no_picture = django_settings.STATIC_URL + 'img/user.png'
        try:
            filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = django_settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                return no_picture
        except Exception as e:
            return no_picture