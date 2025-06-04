from rest_framework import serializers
from .models import Employee, Department, Position, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    # status = serializers.SlugRelatedField(
    #     queryset=Status.objects.all(),
    #     slug_field='name'
    # )
    # position = serializers.SlugRelatedField(
    #     queryset=Position.objects.all(),
    #     slug_field='name'
    # )
    # department = serializers.SlugRelatedField(
    #     queryset=Department.objects.all(),
    #     slug_field='name'
    # )

    class Meta:
        model = Employee
        fields = '__all__'
