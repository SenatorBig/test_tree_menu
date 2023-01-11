from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    left_key = models.IntegerField(null=True, blank=True)
    right_key = models.IntegerField(null=True, blank=True)
    level = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey("Item", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ("name", "menu")

    def __str__(self):
        return self.name
