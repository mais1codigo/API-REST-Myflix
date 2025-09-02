from django.contrib import admin
from Myflix.models import User, Stream

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(User, UserAdmin)


class StreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo',)

admin.site.register(Stream, StreamAdmin)
