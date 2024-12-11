from django.db import models
import helpers
from cloudinary.models import CloudinaryField


helpers.cloudinary_init()

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField(
        "image", 
        null=True
    )
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
        )

    def get_display_name(self):
        return f"{self.title} - Course"

    def get_thumbnail(self):
        if not self.image:
            return None
        return helpers.get_cloudinary_image_object(
            self, 
            field_name='image',
            as_html=False,
            width=382
        )

    def get_display_image(self):
            if not self.image:
                return None
            return helpers.get_cloudinary_image_object(
                self, 
                field_name='image',
                as_html=False,
                width=750
            )

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField("image", 
                tags = ['thumbnail', 'lesson'],
                blank=True, null=True)
    video = CloudinaryField("video",             
            blank=True, 
            null=True, 
            type='private',
            tags = ['video', 'lesson'],
            resource_type='video')
    order = models.IntegerField(default=0)
    can_preview = models.BooleanField(default=False, help_text="If user does not have access to course, can they see this?")
    status = models.CharField(
        max_length=10, 
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order','-updated']

"""
- Lessons
    - Title
    - Description
    - Video
    - Status: Published, Coming Soon, Draft
"""


