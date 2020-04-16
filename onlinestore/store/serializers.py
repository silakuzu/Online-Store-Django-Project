from rest_framework import serializers
from store.models import categories

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'