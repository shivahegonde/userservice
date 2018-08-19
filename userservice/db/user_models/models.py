# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import  uuid
from django.db import models
from datetime import datetime
from flask import request
# Create your models here.



class User(models.Model):
    username=models.CharField(max_length=128,primary_key=True)
    password=models.CharField(max_length=128,null=False)
    first_name=models.CharField(max_length=128)
    middle_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    gender=models.CharField(max_length=128)
    phone=models.IntegerField()
    city=models.CharField(max_length=128)

class Login(models.Model):
    user = models.ForeignKey(User)
    login_time=models.DateTimeField(default=datetime.now())
    token=models.CharField(max_length=128,default=str(uuid.uuid4()))
    logout_time=models.DateTimeField(null=True)
    is_active=models.BooleanField(default=True)
    device_id=models.CharField(max_length=128)