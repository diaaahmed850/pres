from rest_framework import serializers
from .models import stock
class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model=stock
        fields=('ticker','volume')
        #fields=(__all__)