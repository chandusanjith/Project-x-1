
   
from rest_framework import serializers

from .models import *

class rolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'