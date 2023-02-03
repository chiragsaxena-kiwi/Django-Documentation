from rest_framework import serializers  
from .models import Students ,Employee,Todo
  
class StudentSerializer(serializers.ModelSerializer):  

    class Meta:
        model=Students
        fields='__all__' 
  
    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Students.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.address = validated_data.get('address', instance.address)  
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)  
        instance.mobile = validated_data.get('mobile', instance.mobile)  
  
        instance.save()  
        return instance  





class EmployeeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Employee
        fields="__all__"


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields ="__all__"      
        
