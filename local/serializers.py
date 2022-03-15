from dataclasses import fields
from rest_framework import serializers
from local.models import Local
from endereco.serializers import EnderecoSerializer

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        exclude = ('tipo', 'titulo', "numero", "endereco",)

class LocalSerializerRetrieve(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Local
        fields = ("tipo", "titulo", "numero", "endereco",)