from django.contrib import admin
from landpage.models import registerCandidate, gerenciadeVagas

admin.site.site_header = 'Atacale-Vagas ADMIN'
admin.site.index_title = 'Gerenciamento de registros'
admin.site.enable_nav_sidebar = True


class registerCandidateAdmin(admin.ModelAdmin):
    list_display =('cargo', 'nome_completo', 'escolaridade', 'primeiro_emprego', 'idade')
    list_filter = ['cargo', 'primeiro_emprego']
    list_per_page = 20
    search_fields = ['nome_completo']
    
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(registerCandidate, registerCandidateAdmin)


class gerenciadeVagasAdmin(admin.ModelAdmin):
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(gerenciadeVagasAdmin, self).get_form(request, obj, **kwargs)
        for fields in form.base_fields:
            form.base_fields[fields].required = False
        
        return form

admin.site.register(gerenciadeVagas, gerenciadeVagasAdmin)