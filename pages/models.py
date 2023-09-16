import uuid
from django.db import models
from django.utils import timezone

class Partner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Network(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Affiliate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Affiliate Organizations"

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    sent_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.lname.upper()}, {self.fname}"
    

class Donation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)
    sender = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    ref = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    cause = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)
    tx_ref = models.CharField(max_length=200, blank=True, null=True)
    paid_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender