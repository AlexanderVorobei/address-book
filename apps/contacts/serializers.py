from rest_framework import serializers
from .models import Contact


class GetUserMixin:
    def get_user_from_request(self):
        return getattr(self.context.get("request"), "user", None)


class ContactSerializer(GetUserMixin, serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Contact
        fields = (
            "id",
            "user",
            "first_name",
            "last_name",
            "phone",
            "country",
            "city",
            "street",
            "building",
            "floor",
            "url",
            "image",
        )

    def validate_contacts(self, value):
        user = self.get_user_from_request()
        if not user:
            raise serializers.ValidationError("Can't find user.")
        if not self.instance:
            if user not in value:
                raise serializers.ValidationError(
                    "Permissions denied."
                )
        return value

    def create(self, validated_data):
        user = self.get_user_from_request()
        validated_data.update(user=user)
        return super().create(validated_data=validated_data)
