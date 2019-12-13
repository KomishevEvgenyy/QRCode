from django.db import models
import uuid

from .choices import STATUSES
from .manager import QRCodeManager


class QRCode(models.Model):
    image = models.ImageField(upload_to="")  # поле для загрузки картинки
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # поле для создания уникального id
    zone = models.ForeignKey('QRZone', on_delete=models.CASCADE, null=True)  # добавления поля выбора зоны
    name = models.CharField(max_length=256)  # имя зоны
    is_active = models.BooleanField(default=True)  # статус активности
    objects = models.Manager()  #
    active_objects = QRCodeManager()

    def __str__(self):
        return self.name


class QRZone(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    qr_id = None
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=48)
    status = models.IntegerField(choices=STATUSES, default=1)

    def __str__(self):
        return self.name


