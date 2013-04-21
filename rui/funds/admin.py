from django.contrib import admin
from funds.models import Hedgerahastot, Korkorahastot, Osakerahastot, Yhdistelmarahastot, Luokittelemattomat

all = [Hedgerahastot, Korkorahastot, Osakerahastot, Yhdistelmarahastot, Luokittelemattomat]

for model in all:
    admin.site.register(model)
