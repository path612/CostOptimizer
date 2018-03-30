from django.contrib import admin
from .models import *

admin.site.register(ProductCatagory)
admin.site.register(OriginCity)
admin.site.register(PortCity)
admin.site.register(DestinationCity)
admin.site.register(OriginToPortRoad)
admin.site.register(OriginToPortRail)
admin.site.register(OriginToPortAir)
admin.site.register(PortToDestinationAir)
admin.site.register(PortToDestinationRoad)
admin.site.register(PortToDestinationSea)