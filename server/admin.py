from django.contrib import admin
from server.models import models

from .models import customer
from .models import notes
from .models import trends
admin.site.register(notes)
admin.site.register(trends)
admin.site.register(customer)