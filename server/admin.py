from django.contrib import admin

from .models import customer
from .models import notes
from .models import relation
from .models import trends

admin.site.register(notes)
admin.site.register(trends)
admin.site.register(customer)
admin.site.register(relation)
