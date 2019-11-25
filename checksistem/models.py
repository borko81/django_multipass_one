from django.db import models

# Модел за групите


class WorkGroups(models.Model):

    group_name = models.CharField(max_length=20, unique=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.group_name


# Модел за картите
class Cards(models.Model):

    card = models.CharField(max_length=10)

    def __str__(self):
        return self.card


# Модел за служителите
class Employe(models.Model):

    employe_name = models.CharField(max_length=50, unique=True, blank=True)
    group_employe = models.ForeignKey(WorkGroups, on_delete=models.CASCADE)
    card_employe = models.ForeignKey(Cards, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employe_name}"
