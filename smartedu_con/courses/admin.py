# courses/admin.py
from django.contrib import admin
from .models import Course   # yalnızca Course modelini import et

@admin.register(Course)       # dekoratör veya alttaki register yöntemi, ikisinden biri yeter
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "available",)        # modeldeki alan adın neyse onu kullan
    list_filter = ("available",)
    list_display_links = ("name",)
    search_fields = ('name', 'description', )


