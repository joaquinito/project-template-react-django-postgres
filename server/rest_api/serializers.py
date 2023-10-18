from rest_framework import serializers
from .models import Vehicle

# Serializers are a way to convert objects to and from Python objects. It takes a JSON input that
# might be posted from the API, validates the input to make sure that it is secure and correct as
# per our validation rules and then it converts it either to a Python object or a model in our 
# actual database. It also does the reverse, which is to convert a Python object or a model to a
# JSON output. 

class VehicleSerializer(serializers.ModelSerializer):

    numberWheels = serializers.IntegerField(source='number_wheels')

    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'type', 'numberWheels']
        read_only_fields = ['id']
