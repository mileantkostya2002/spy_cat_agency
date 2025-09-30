from rest_framework import serializers
from .models import SpyCat, Mission, Target, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class SpyCatMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['name', 'breed']

class SpyCatListSerializer(serializers.ModelSerializer):
    breed = serializers.CharField(
        source="breed.name",
        write_only=True
    )
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']


class SpyCatUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['salary']

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']

class TargetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


    def validate(self, data):
        if self.instance:
            if 'notes' in data and data['notes'] != self.instance.notes:
                if self.instance.is_complete:
                    raise serializers.ValidationError("Cannot update notes: target is complete")
                if self.instance.mission.is_complete:
                    raise serializers.ValidationError("Cannot update notes: mission is complete")
        return data

class TargetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes']

class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'notes', 'country', 'is_complete']

class TargetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'notes']

class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'target', 'is_complete', 'created_at', 'updated_at']
        read_only_fields = ['id', 'is_complete', 'created_at', 'updated_at']


class MissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'cat', 'target', 'created_at']
        read_only_fields = ['id', 'created_at']

class MissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'cat', 'target', 'is_complete']


class MissionListSerializer(serializers.ModelSerializer):
    cat = SpyCatMissionSerializer()
    target = TargetSerializer()

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'target', 'is_complete']

class MissionDetailSerialize(serializers.ModelSerializer):
    cat = SpyCatMissionSerializer()
    target = TargetSerializer()

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'target', 'is_complete', 'created_at', 'updated_at']


class MissionAssignCatSerializer(serializers.Serializer):
    cat_id = serializers.IntegerField()

    def validate_cat_id(self, value):
        try:
            cat = SpyCat.objects.get(id=value)
        except SpyCat.DoesNotExist:
            raise serializers.ValidationError("Cat not found")


        if Mission.objects.filter(cat=cat, is_complete=False).exists():
            raise serializers.ValidationError("Cat already has an active mission")

        return value

class MissionUniqueTargetSerializer(serializers.Serializer):
    target_id = serializers.IntegerField()

    def validate_target(self, value):
        try:
            target = Target.objects.get(id=value)
        except Target.DoesNotExist:
            raise serializers.ValidationError("Cat not found")


        if Mission.objects.filter(cat=target, is_complete=False).exists():
            raise serializers.ValidationError("Target already in active mission")

        return value