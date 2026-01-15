age = 18
permis = False
casier_vierge = True

peut_conduire = (age >= 18) and permis
print(peut_conduire)

peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print(peut_louer_voiture)

sanction = not casier_vierge
print(sanction)
