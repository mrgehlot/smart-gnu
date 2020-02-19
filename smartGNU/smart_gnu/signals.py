from django.db.models.signals import pre_save, post_save
from .models import Device

# def add_topic(instance, **kwargs):
#     instance.topic = "{}/{}".format(instance.lab.lab_number,instance.device_name)
# pre_save.connect(add_topic,sender=Device)