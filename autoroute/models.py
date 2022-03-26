from django.db import models


class AutoroutingModel(models.Model):

    url_format = '%s/<%s:%s>/'
    model_views = ['view']

    class Meta:
        abstract = True
