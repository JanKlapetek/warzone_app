# loadouts/seed.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'warzone_app.settings')
django.setup()

from loadouts.models import Category, Weapon, Perk, Loadout
from django.db import transaction

@transaction.atomic
def run():
    print("⏳ Mažu stará data...")
    Loadout.objects.all().delete()
    Weapon.objects.all().delete()
    Perk.objects.all().delete()
    Category.objects.all().delete()

    print("📦 Přidávám kategorie...")
    ar = Category.objects.create(name="Assault Rifle")
    smg = Category.objects.create(name="SMG")

    print("🔫 Přidávám zbraně...")
    m4 = Weapon.objects.create(name="M4A1", category=ar)
    mp5 = Weapon.objects.create(name="MP5", category=smg)

    print("🧠 Přidávám perky...")
    ghost = Perk.objects.create(name="Ghost")
    overkill = Perk.objects.create(name="Overkill")

    print("🎒 Přidávám loadouty...")
    stealth = Loadout.objects.create(name="Stealth Master", weapon=m4)
    stealth.perks.set([ghost, overkill])

    rusher = Loadout.objects.create(name="Fast Rusher", weapon=mp5)
    rusher.perks.set([overkill])

    print("✅ Hotovo! Data byla úspěšně přidána.")

# Spusť funkci
if __name__ == '__main__':
    run()