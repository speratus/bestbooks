from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import Link


class LinkAdmin(ModelAdmin):
    model = Link
    menu_label = 'Links'
    add_to_settings_menu = False
    exclude_from_explorer = False
    search_fields = ('name')


modeladmin_register(LinkAdmin)
