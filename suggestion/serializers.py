from rest_framework import serializers
from .models import Suggestion


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = [
            'id',
            'posted_by',
            'suggestion',
            'is_read'
        ]


        def create(self, validated_data):
            sugestion = Suggestion(
                user_id = validated_data['user_id'],
                suggestion = validated_data['suggestion'],
                is_read = validated_data['is_read']
            )

            suggestion.save()
            return sugestion