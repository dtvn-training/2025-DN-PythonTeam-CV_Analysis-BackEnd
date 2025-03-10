from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from job_description.serializers import JDSerializer
from rest_framework import response, status, permissions
from .models import JD
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Add to views.py
class JobDescriptionListAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        """Get a list of all job descriptions."""
        job_descriptions = JD.objects.filter(status=True)
        serializer = JDSerializer(job_descriptions, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new job description."""
        serializer = JDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobDescriptionDetailAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        """Get a specific job description by ID."""
        try:
            job_description = JD.objects.get(id=id, status=True)
            serializer = JDSerializer(job_description)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Job description not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        """Update a specific job description by ID."""
        try:
            job_description = JD.objects.get(id=id, status=True)
            serializer = JDSerializer(job_description, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Job description not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        """Delete a specific job description by ID."""
        try:
            job_description = JD.objects.get(id=id, status=True)
            job_description.status = False
            job_description.save()
            return JsonResponse({"message": "Job description deleted successfully."}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "Job description not found."}, status=status.HTTP_404_NOT_FOUND)
        
        