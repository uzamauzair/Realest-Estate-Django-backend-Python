from rest_framework import serializers
from .models import Listing

# We will create 2 types of serializers, 1 to return all the fields and other to return specific set of fields
# the one which going to return specific set of fields when we search for listings
# to see all the criteria of particular listings then you can use all the fields

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title','address','city','state','price','sale_type','home_type', 'bedrooms','bathrooms','sqft','photo_main','slug')
        # by using slug, we can use a view button and direct to correct url

class ListingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'