from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    name = models.CharField(max_length=100)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Perk(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Loadout(models.Model):
    name = models.CharField(max_length=100)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    attachments = models.ManyToManyField(Attachment, blank=True)
    perks = models.ManyToManyField(Perk, blank=True)

    def __str__(self):
        return self.name