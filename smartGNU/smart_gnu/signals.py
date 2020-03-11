from django.db.models.signals import pre_save, post_save
from .models import Device
from .mqtt_code import request_for_publish
from .models import GPIO_PINS,NodeMCU
from django.db import transaction
def add_topic(instance, **kwargs):
    instance.topic = instance.node_mcu.node_mcu_ip
pre_save.connect(add_topic,sender=Device)

# def publish_topic(instance,created,**kwargs):
#     if created:
#         request_for_publish(topic=instance.lab.lab_number.replace(" ",""),pay_load=instance.device_name.replace(" ",""))
# post_save.connect(publish_topic,sender=Device)

def add_devices(instance,created,**kwargs):
    with transaction.atomic():
        if created:
            for i in range(1,len(GPIO_PINS)+1):
                Device.objects.get_or_create(device_name ="{}-{}".format(instance.lab.lab_number,i),
                                      topic = instance.node_mcu_ip, gpio_pin = i,
                                      node_mcu = instance)
post_save.connect(add_devices,sender=NodeMCU)