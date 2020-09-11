from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post #specifying Model class to take data from
        fields =('id','title','message') #JSON response keys