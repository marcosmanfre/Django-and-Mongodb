from rest_framework import serializers
from djangoapp.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining')