from django.contrib import admin

from .models import *



class VendeurAdmin(admin.ModelAdmin):
    list_display = ('id','prenom','nom','adresse','telephone','sexe')

admin.site.register(Vendeur, VendeurAdmin)



class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','vendeur','nom','date_creation','date_expiration')

admin.site.register(Produit, ProduitAdmin)

# Register your models here.
