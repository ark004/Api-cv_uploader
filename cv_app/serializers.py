from rest_framework import serializers
from cv_app.models import prof

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        models=prof
        fields=['id','name','email','dob','state',
        'gender','location','piimage','docfile']
