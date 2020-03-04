from django.db.models.signals import pre_save, post_save
from .models import Device
from .mqtt_code import request_for_publish

def add_topic(instance, **kwargs):
    instance.topic = instance.device_name.replace(" ","")
pre_save.connect(add_topic,sender=Device)

def subscribe_topic(instance,created,**kwargs):
    if created:
        request_for_publish(topic=instance.lab.lab_number.replace(" ",""),pay_load=instance.device_name.replace(" ",""))
post_save.connect(subscribe_topic,sender=Device)