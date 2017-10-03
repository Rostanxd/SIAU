from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

ACTIVE = 'A'
FINISHED = 'F'
CANCELED = 'C'

STATES = [
    (ACTIVE, 'Activo'),
    (CANCELED, 'Cancelado'),
    (FINISHED, 'Finalizado'),
]


class Request(models.Model):
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=60)
    description = models.TextField()
    state = models.CharField(max_length=1, choices=STATES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def state_name(self):
        if self.state == 'A':
            return 'Activo'
        elif self.state == 'F':
            return 'Finalizado'
        else:
            return 'Cancelado'

    def __str__(self):
        return self.subject


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['email', 'subject', 'description', 'state']

