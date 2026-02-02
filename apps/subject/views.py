from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Class, Subject
from .serializers import ClassSerializer, SubjectSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class ClassApiView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]  

    def get(self, request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubjectApiView(APIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]  

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_staff:
            return Response({"error": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return None

    def get(self, request, pk):
        subject = self.get_object(pk)
        if not subject:
            return Response({"error": "Subject not found"}, status=404)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        subject = self.get_object(pk)
        if not subject:
            return Response({"error": "Subject not found"}, status=404)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "You are not authorized"}, status=status.HTTP_403_FORBIDDEN)
        subject = self.get_object(pk)
        if not subject:
            return Response({"error": "Subject not found"}, status=404)
        subject.delete()
        return Response({"message": "Deleted successfully"}, status=204)
