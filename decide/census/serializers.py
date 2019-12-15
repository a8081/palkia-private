
from rest_framework import serializers

from .models import Census

class CensusSerializer(serializers.HyperlinkedModelSerializer):
  voters = serializers.IntegerField()
  voting_id = serializers.IntegerField()
  class Meta:
    model = Census
    fields =('voting_id','voters')