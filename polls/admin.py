from django.contrib import admin

# Register your models here.

from .models import Question

# register Question to administrator
admin.site.register(Question)
# register Choice to administrator

from .models import Choice

admin.site.register(Choice)