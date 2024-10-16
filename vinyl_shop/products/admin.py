from django.contrib import admin
from products.models import Genre, Artist, Label, Album, Track

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Label)
admin.site.register(Album)
admin.site.register(Track)

