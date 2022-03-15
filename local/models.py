from django.db import models
from django_extensions.db.models import TimeStampedModel
from endereco.models import Endereco

class Local(TimeStampedModel):

    titulo = models.CharField (
         db_column="TITULO",
         max_length=100,
    )

    tipo = models.CharField (
         db_column="TIPO",
         max_length=100,
    )

    numero = models.CharField (
         db_column="NUMERO",
         max_length=10,
    )

    endereco = models.OneToOneField (
        to=Endereco,
        on_delete=models.DO_NOTHING, db_column="ENDERECO"
    )

    class Meta:
        db_table = "LOCAL"
        verbose_name = "local"
        verbose_name_plural = "locais"
