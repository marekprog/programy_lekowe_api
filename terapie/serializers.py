from rest_framework import serializers
from .models import Therapy
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class TherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapy
        fields = ('id','name','rozpoznanie','mutacja_aktywujaca_EFGR','zaawansowanie','zmiany_mierzalne','brak_przerzutow_OUN',
                  'stopien_sprawnosci','wczesniejsze_leczenie_systemowe_zp_raka_pluca','wczesniejsze_leczenie_systemowe_zp_raka_pluca_incl_anty_ALK',
                  'wykluczenie_przeciwwskazan','progresja_po_leczeniu_innym_inhibitorem_EFGR','mutacja_T790_w_genie_EGFR',
                  'Obecnosc_rearanzacji_w_genie_ALK_lub_ROS1','wczesniejsze_leczenie_systemowe_kryzotynibem')
        def create(self,validated_data):
            return Therapy(**validated_data)

