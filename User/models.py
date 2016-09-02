from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=128)

    def __init__(self, **kwargs):
        models.Model.__init__(self)
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def __repr__(self):
        return '<User %s>' % self.username

    def verify_password(self, password):
        if password == self.password_hash:
            return True
        else:
            return False

    def changepassword(self, password):
        self.password_hash = password
        return True