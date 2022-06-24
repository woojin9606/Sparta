from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from .serializers import JobPostSerializer, CompanySerializer, JobPostSkillSetSerializer
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)
        #jobpostskillset = JobPostSkillSet.objects.filter()
        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        print("gdgdgdgd")
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name")

        Job_serializer = JobPostSerializer(data=request.data)

        if Job_serializer.is_valid() and JobType.objects.get(id=job_type) is not None:
            Job_serializer.save()
            return Response(Job_serializer.data,status=status.HTTP_200_OK)
        return Response(Job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

