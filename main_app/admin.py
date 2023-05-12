from django.contrib import admin
from .models import Game, Reviews, Collectible
# Register your models here.
admin.site.register(Game)
admin.site.register(Reviews)
admin.site.register(Collectible)