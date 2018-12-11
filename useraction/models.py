from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Dict, Any


class User(AbstractUser):
    email = models.EmailField(blank=False)
    introduction = models.TextField(default='')
    school = models.CharField(default='', max_length=64)

    # need to set this or cannot create super user
    individual = models.BooleanField(default=True)

    def to_dict(self, detail: bool=False) -> Dict[str, Any]:
        return {
            'username': self.username,
            'email': self.email,
            'introduction': self.introduction,
            'school': self.school,
            'individual': int(self.individual)
        }
