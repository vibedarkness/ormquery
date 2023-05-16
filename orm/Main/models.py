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
    



class Vendeur(models.Model):
    sexechoice=(
        ("Masculin","M"),
        ("Feminin","F")

    )

    prenom = models.CharField(max_length = 150)
    nom = models.CharField(max_length = 150)
    adresse = models.CharField(max_length = 150)
    telephone = models.CharField(max_length = 150)
    sexe = models.CharField(max_length = 15, choices=sexechoice, default="Masculin")
    
    

    def __str__(self):
        return self.prenom
    


class Produit(models.Model):
    vendeur=models.ForeignKey(Vendeur, on_delete=models.CASCADE)
    nom = models.CharField(max_length = 150)
    date_creation = models.DateField(auto_now=False, auto_now_add=False)
    date_expiration = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    

    def __str__(self):
        return self.nom

    


    

