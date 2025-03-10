from rest_framework import serializers
from .models import JD
from authentication.models import User

class JDSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    
    class Meta:
        model = JD
        fields = ['id', 'title', 'description', 'requirements', 'compulsory', 
                  'benefits', 'salary', 'tag', 'status', 'user_id', 'user_email',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_email']
    
    def get_user_email(self, obj):
        """Get the email of the user who created the job description."""
        if obj.user_id:
            return obj.user_id.email
        return None
    
    def validate_salary(self, value):
        """Validate that salary is a positive integer."""
        if value < 0:
            raise serializers.ValidationError("Salary must be a positive value.")
        return value
    
    def validate_compulsory(self, value):
        """Validate that compulsory is a valid JSON array."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Compulsory fields must be a list.")
        return value
    
    def validate_tag(self, value):
        """Validate that tag is a valid JSON array."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Tags must be a list.")
        return value