from rest_framework import serializers
from .models import Training_Enquiry,Development_Enquiry

#get api
class Training_EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Training_Enquiry
        fields='__all__'

class Development_EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Development_Enquiry
        fields='__all__'