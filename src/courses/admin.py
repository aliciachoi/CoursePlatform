import helpers
from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Lesson
# Register your models here.

class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ['updated']
    extra = 0

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'status', 'access']
    list_filter = ['status', 'access']
    fields = [ 'title', 'description', 'status', 'image', 'access', 'display_image']
    readonly_fields = ['display_image']

    def display_image(self, obj, *args, **kwargs):
        url = helpers.get_cloudinary_image_object(
            obj, 
            field_name='image',
            width=200
        )
        return format_html(f"<img src={url} />")

    display_image.short_description = "Current Image"