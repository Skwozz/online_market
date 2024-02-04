from abc import ABC

from rest_framework import serializers, validators

from api.models import User, Warehouse, Product, Purchase


class UserSerializer(serializers.Serializer):
    SECTION = [('PR', 'provider'), ('CL', 'client')]
    username = serializers.CharField(max_length=64, validators=[validators.UniqueValidator(User.objects.all())])
    email = serializers.EmailField(max_length=64, validators=[validators.UniqueValidator(User.objects.all())])
    password = serializers.CharField(min_length=6, max_length=12, write_only=True)
    type_user = serializers.ChoiceField(choices=SECTION)

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])

        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])

        if type_user := validated_data.get("password"):
            instance.type_user = type_user
            instance.save(update_fields=["type_user"])
        return instance

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            type_user=validated_data["type_user"]
        )
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class WarehouseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64, validators=[validators.UniqueValidator(Warehouse.objects.all())])

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    # def update(self, instance, validated_data):
    #     if name := validated_data.get("name"):
    #         instance.name = name
    #         instance.save(update_fields=["name"])
    #     return instance
    # def create(self, validated_data):
    #     warehouse = Warehouse.objects.create(
    #         name=validated_data["name"]
    #     )
    #     warehouse.save()
    #     return warehouse

    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    quantity = serializers.IntegerField()
    warehouse = Warehouse.objects.get(id=1)
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data["name"],
            quantity=validated_data["quantity"],
            warehouse=validated_data["warehouse"]
        )

        product.save()
        return product


    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class PurchaseSerializer(serializers.Serializer):
    product = serializers.CharField(max_length=64, )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        model = Purchase
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
