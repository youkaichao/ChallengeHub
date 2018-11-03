from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False)
    introduction = models.TextField(default='')
    school = models.CharField(default='', max_length=64)

    # need to set this or cannot create super user
    individual = models.BooleanField(default=True)

    def to_dict(self):
        return {
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'introduction': self.introduction,
            'school': self.school,
            'isIndividual': self.individual
        }
