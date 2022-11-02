
from rest_framework.response import Response
from cv_app.models import prof
from cv_app.serializers import ProfileSerializers
from rest_framework.views import APIView
from rest_framework import status, serializers


class ProfileView(APIView):
    def post(self,request,format=None):
        Serializer = ProfileSerializers(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({
                'msg':'Resume uploaded successfully',
                'status':'success','candidate':'serializer.data'
            },status=status.HTTP_201_CREATED)
        return Response(serializers.errors)
    def get(self,request,format=None):
        candidates =prof.objects.all()
        Serializer =ProfileSerializers(candidates,many=True)
        return Response({'status':'succes','candidates':serializers.data},status=status.HTTP_200_OK)