from rest_framework import serializers
from api.models import CommAppLoginMaster,CommDeptMaster,CommDesigMaster,CommAppLogin,CommBldgMaster,ComplaintDirectorate,ComplainCasetypeMaster,ComplaintAreaCategory,Empdetail

class CommAppLoginMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommAppLoginMaster
        # feilds= '__all__'
        fields = '__all__'
   
class CommAppLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommAppLogin
        fields = '__all__'
  
class CommDeptMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommDeptMaster
        fields = '__all__'

class CommDesigMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommDesigMaster
        fields = '__all__'
        
class CommBldgMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommBldgMaster
        fields = '__all__'
        
class ComplaintDirectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplaintDirectorate
        fields = '__all__'
class ComplainCasetypeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplainCasetypeMaster
        fields = '__all__'
class ComplaintAreaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplaintAreaCategory
        fields = '__all__'

class EmpdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empdetail
        # feilds= '__all__'
        fields = '__all__'