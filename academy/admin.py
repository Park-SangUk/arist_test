from django.contrib import admin
from academy.models import Level, Contents, Images

# Register your models here.


class ImagesInline(admin.StackedInline):
    model = Images
    extra = 1


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)
    list_display = ('id', 'title', 'upload_dt')
