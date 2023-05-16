from django.db import models

# Create your models here.


class Teacher(models.Model):
    prenom = models.CharField(max_length = 150)
    nom = models.CharField(max_length = 150)
    adresse = models.CharField(max_length = 150)
    telephone = models.CharField(max_length = 150)
    sexe = models.CharField(max_length = 150)

    def __str__(self):
        return self.prenom

class Student(models.Model):
    prenom = models.CharField(max_length = 150)
    nom = models.CharField(max_length = 150)
    adresse = models.CharField(max_length = 150)
    telephone = models.CharField(max_length = 150)
    sexe = models.CharField(max_length = 150)
    age=models.IntegerField()
    classe=models.IntegerField(null=True,default=0)
    teacher = models.CharField(max_length = 150,null=True,default="")

    def __str__(self):
        return self.prenom

