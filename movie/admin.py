from django.contrib import admin


from .models import category,moviedb,trailer,payment

admin.site.register(category)
admin.site.register(trailer)
admin.site.register(moviedb)
admin.site.register(payment)

