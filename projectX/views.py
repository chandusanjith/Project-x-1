from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class GetRolesView(APIView):
  serializer_class = rolesSerializer

  def get(self, request, format=None):
    try:
        roles = Roles.objects.all()
        if not roles:
          return Response({
          "ERROR":"404 NO DATA FOUND :("}, status=status.HTTP_404_NOT_FOUND)
        roles_serializer = rolesSerializer(roles, many=True).data
        return Response(roles_serializer, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      return Response({
          "ERROR":"OOps!! something went wrong!!"}, status=status.HTTP_404_NOT_FOUND)
  