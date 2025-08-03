from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.db import models

# List of models to watch
from .models import AboutSection, Post, Work, WorkDetail, Service, Category

# 🔁 Helper to get image fields
def get_image_fields(instance):
    return [field.name for field in instance._meta.fields if isinstance(field, models.ImageField)]

# ✅ Delete old file when updating
@receiver(pre_save)
def auto_delete_old_file_on_change(sender, instance, **kwargs):
    if not hasattr(instance, 'pk') or not instance.pk:
        return  # New instance, nothing to delete

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    for field_name in get_image_fields(instance):
        old_file = getattr(old_instance, field_name)
        new_file = getattr(instance, field_name)

        if old_file and old_file != new_file:
            old_file.delete(save=False)

# ✅ Delete files when instance is deleted
@receiver(post_delete)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    for field_name in get_image_fields(instance):
        file = getattr(instance, field_name)
        if file:
            file.delete(save=False)
