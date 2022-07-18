from django.db import models
from account.models import Account
from datetime import date


class system_settings(models.Model):
    DIRECTIONS = (
        ('horizontal', 'horizontal'),
        ('vertical', 'vertical')
    )
    LABELS = (
        ("text","text"),
        ("image","image")
    )
    name = models.CharField(max_length=500)
    orientation = models.CharField(max_length=10, choices=DIRECTIONS)
    numberrating = models.IntegerField()
    scalecolor = models.CharField(max_length=20)
    roundcolor = models.CharField(max_length=20)
    fontcolor = models.CharField(max_length=20)
    fomat = models.CharField(max_length=500)
    # label = models.CharField(choices=LABELS, max_length=10)
    left = models.CharField(max_length=50)
    right = models.CharField(max_length=50)
    center = models.CharField(max_length=50, blank=True)
    time = models.IntegerField(blank=True)
    text = models.CharField(max_length=500, blank=True)
    template_name = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"

    # def save(self, *args, **kwargs):
    #     x = date.today()
    #     self.template_name =  f'{self.name}{x}'
    #     super(system_settings, self).save(*args, **kwargs)


class response(models.Model):
    score = models.IntegerField()
    category = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        if self.score <= 6:
            self.category = "Detractor"
        elif self.score <= 8:
            self.category = "Neutral"
        else:
            self.category = "Promoter"
        super(response, self).save(*args, **kwargs)
