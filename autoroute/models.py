from django.db import models

from autoroute.helpers import ViewType


class AutoroutingModel(models.Model):

    url_format = '%s/<%s>/'
    model_views = list[ViewType]

    class Meta:
        abstract = True
