from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Company
from api.serializers import CompanySerializer

class CompanyListApi(generics.ListCreateAPIView):
    # queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompanyDeatailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_url_kwarg = 'company_id'
    permission_classes = (IsAuthenticated)

