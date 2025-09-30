
from django.db import models


class Breed(models.Model):
    name = models.CharField(blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class SpyCat(models.Model):
    name = models.CharField(blank=False, null=False)
    years_of_experience = models.IntegerField()
    salary = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.breed}'

class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True, default='')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.country}'

class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)