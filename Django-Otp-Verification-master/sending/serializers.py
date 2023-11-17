from rest_framework import serializers 
from .models import FieldsToBeSent

class FieldsToBeSentSerializers (serializers.ModelSerializer):
    class Meta:
        model=FieldsToBeSent
        fields=['id','number']