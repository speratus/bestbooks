from django.db import models


class AutoroutingModel(models.Model):

    model_views = []
    # TODO: refactor this model so that it can be deleted.

    class Meta:
        abstract = True

