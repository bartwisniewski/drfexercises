from django.db import models

MODES = (('off', 'OFF'), ('man', 'MANUAL'), ('auto', 'AUTO'))


class ProcessObject(models.Model):
    tag = models.CharField(max_length=100)
    mode = models.CharField(max_length=4, choices=MODES, default='off')

    class Meta:
        abstract = True


class Valve(ProcessObject):
    open = models.BooleanField(default=False)
    feedback_open = models.BooleanField(default=False)
    feedback_close = models.BooleanField(default=True)
    time_monitoring = models.FloatField(default=5.0)


class Pump(ProcessObject):
    on = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    max_pressure = models.FloatField(default=5.0)
    nominal_flow = models.FloatField(default=10.0)
