from django.db import models
from django.contrib import admin
from models import Weapon, Attachment, Loadout, Perk, Category

admin.site.register(Weapon)
admin.site.register(Attachment)
admin.site.register(Loadout)
admin.site.register(Perk)
admin.site.register(Category)

