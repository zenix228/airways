from django.db.models import *

class Plane(Model):
    name = CharField(max_length=150)
    characterictics = TextField(blank=True, null=True)
    capacity = IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'