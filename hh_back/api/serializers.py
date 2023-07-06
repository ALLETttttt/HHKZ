from rest_framework import serializers
from api.models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    user = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField(required=False)

    def create(self, data):
        company = Company.objects.create(**data)
        return company
    
    def update(self, instance, newData):
        instance.name = newData.get('name', instance.name)
        instance.description = newData.get('description', instance.description)
        instance.city = newData.get('city', instance.city)
        instance.save()
        return instance

class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'user', 'name', 'city', 'address')



class VacancyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'salary', 'company_id')