from django.db.models import *

from apps.plane.models import Plane

class Airline(Model):
    name = CharField(max_length=511)
    created_at = DateField(blank=True, null=True)
    planes = ManyToOneRel(to='apps.plane.models.Plane', on_delete=CASCADE, related_name='planes', field='plane', field_name='plane')

    def __str__(self):
        return f'{self.name}'
