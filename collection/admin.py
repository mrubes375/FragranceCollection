from django.contrib import admin
from .models import Fragrance, Base_Note, Heart_Note, Top_Note
# Register your models here.
class FragranceAdmin(admin.ModelAdmin):
    list_display = ['name', 'house', 'perfumer', 'size']
    list_filter = ['house', 'perfumer']
    search_fields = ['name', 'perfumer', 'house']
    class Meta:
        model = Fragrance


admin.site.register(Fragrance, FragranceAdmin)
