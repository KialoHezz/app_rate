from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["id","user",'bio', 'contact','image']
