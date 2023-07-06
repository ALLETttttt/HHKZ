import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Vacancy
from api.serializers import VacancyModelSerializer

class VacancyListApi(APIView):
    def get(self, request):
        vacancy = Vacancy.objects.all()
        serializer_vacancy = VacancyModelSerializer(vacancy, many=True)
        # vacancy_json = [p.to_json() for p in vacancy]
        return Response(serializer_vacancy.data)
    

    def post(self, request):
        serializer = VacancyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VacancyDetailApi(APIView):
    def get_object(self, vacancy_id):
        try:
            return Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return Response({'Error': str(e)})
        
    def get(self, request, vacancy_id):
        instance = self.get_object(vacancy_id)
        serializer = VacancyModelSerializer(instance)
        return Response(serializer.data)
        
    def put(self, request, vacancy_id):
        instance = self.get_object(vacancy_id)
        serializer = VacancyModelSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, vacancy_id):
        instance = self.get_object(vacancy_id)
        instance.delete()
        return Response({'Deleted': True})