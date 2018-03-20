#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Vol(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/img')
    disc = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"


class Donate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=20)
    comp = models.BooleanField(blank=True)
    sms = models.BooleanField(blank=True)
    date = models.DateField(blank=True, default=timezone.now)
    time = models.TimeField(blank=True, default=datetime.datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пожертвование"
        verbose_name_plural = "Пожертвования"


class Volunteer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=20)
    date = models.DateField(blank=True, default=timezone.now)
    time = models.TimeField(blank=True, default=datetime.datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка на волонтерство"
        verbose_name_plural = "Заявки на волонтерство"