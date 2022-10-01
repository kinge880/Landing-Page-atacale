from django.contrib import admin
from landpage.models import registerCandidate, gerenciadeVagas

admin.site.site_header = 'Atacale-Vagas ADMIN'
admin.site.index_title = 'Gerenciamento de registros'
admin.site.enable_nav_sidebar = True


class registerCandidateAdmin(admin.ModelAdmin):
    list_display =('cargo', 'nome_completo', 'escolaridade', 'idade')
    list_filter = ['cargo']
    list_per_page = 10
    search_fields = ['cargo']

admin.site.register(registerCandidate, registerCandidateAdmin)


class gerenciadeVagasAdmin(admin.ModelAdmin):
    pass

admin.site.register(gerenciadeVagas, gerenciadeVagasAdmin)