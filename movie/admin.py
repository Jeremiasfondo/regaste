from django.contrib import admin


from .models import category,movie,trailer,payment

admin.site.register(category)
admin.site.register(trailer)
admin.site.register(movie)
admin.site.register(payment)

