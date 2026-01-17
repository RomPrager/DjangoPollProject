from django.contrib import admin
from .models import Question, Choice, Names
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
@admin.register(Names)

class MyModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        # all normal fields + many-to-many fields
        return [f.name for f in self.model._meta.fields] + \
               [m.name for m in self.model._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        # allow opening objects, but not editing/saving
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions.pop("delete_selected", None)
        return actions

