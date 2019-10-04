from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128)

    # def __str__(self):
    #     return 'User: {}'.format(self.user_name)

    class Meta:
        app_label = 'admin_main'
        db_table = 'user'

