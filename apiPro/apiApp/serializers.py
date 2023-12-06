from  rest_framework import serializers
from .models import Employee 
 
class Employeeserializers(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = ['id','name','domain','company']