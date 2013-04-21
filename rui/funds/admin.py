from django.contrib import admin
from funds.models import Hedge, Bond, Stock, Balanced, Unclassified

all = [Hedge, Bond, Stock, Balanced, Unclassified]

for model in all:
    admin.site.register(model)
