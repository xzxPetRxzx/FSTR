from rest_framework import serializers
from .models import Users, PerevalAdded, PerevalImages, Coords, Level


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        extra_kwargs = {
            'email': {'validators': []},
        }


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = ('data', 'title')


class PerevalAddedSerializer(serializers.Serializer):
    beauty_title = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=50)
    other_titles = serializers.CharField(max_length=50)
    connect = serializers.CharField(max_length=50, allow_blank=True)
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=['%Y-%m-%d %H:%M:%S', 'iso-8601', ])
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    def create(self, validated_data):
        images = validated_data.pop('images')
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        saved_user = Users.objects.get_or_create(**user)
        saved_coords = Coords.objects.create(**coords)
        saved_level = Level.objects.create(**level)
        pereval = PerevalAdded.objects.create(**validated_data, user=saved_user[0], level=saved_level, coords=saved_coords)
        for image in images:
            PerevalImages.objects.create(**image, pereval_added=pereval)
        return pereval

    def update(self, instance, validated_data):
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')
        coords_obj = instance.coords
        level_obj = instance.level
        images_obj = list((instance.images).all())
        coords_obj.latitude = coords.get("latitude", coords_obj.latitude)
        coords_obj.longitude = coords.get("longitude", coords_obj.longitude)
        coords_obj.height = coords.get("height", coords_obj.height)
        coords_obj.save()
        level_obj.winter = level.get("winter", level_obj.winter)
        level_obj.summer = level.get("summer", level_obj.summer)
        level_obj.autumn = level.get("autumn", level_obj.autumn)
        level_obj.spring = level.get("spring", level_obj.spring)
        level_obj.save()
        for image in images:
            if images_obj:
                image_obj = images_obj.pop(0)
                image_obj.title = image.get("title", image_obj.title)
                image_obj.data = image.get("data", image_obj.data)
                image_obj.save()
            else:
                PerevalImages.objects.create(**image, pereval_added=instance)
        instance.beauty_title = validated_data.get("beauty_title", instance.beauty_title)
        instance.title = validated_data.get("title", instance.title)
        instance.other_titles = validated_data.get("other_titles", instance.other_titles)
        instance.connect = validated_data.get("connect", instance.connect)
        instance.add_time = validated_data.get("add_time", instance.add_time)
        instance.save()
        return instance



class PerevalReadSerializer(serializers.ModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = (
            'id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'other_titles', 'user',
            'coords', 'level', 'images'
        )
