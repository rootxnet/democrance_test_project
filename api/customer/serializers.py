from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'dob'
        ]