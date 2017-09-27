# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# class UserManager(models.Manager):
#     def clean(self):
#         self.cleaned_data = super(self).clean()
#         password = self.cleaned_data.get('password')
#         confirm = self.cleaned_data.get('confirm')
#         if password != confirm:
#             raise forms.ValidationError("Passwords do not match!", code='mismatch')
#         return self.cleaned_data


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()
