# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True


from django.db import models

def save(self, *args, **kwargs):
    self.object_list = ModelName.objects.order_by('auto_inc_id')
    if len(self.object_list) == 0:  # if there are no objects
        self.auto_inc_id = 1
    else:
        self.auto_inc_id = self.object_list.last().auto_inc_id + 1
    super(ModelName, self).save()


class ComappCommAppProfileRetire(models.Model):

    ppo_no = models.CharField(primary_key=True, max_length=14)

    name = models.CharField(max_length=60, blank=True, null=True)

    dob = models.DateField(blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)

    mobno = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    department = models.CharField(max_length=2, blank=True, null=True)

    desig_id = models.CharField(max_length=3, blank=True, null=True)

    gender = models.CharField(max_length=1, blank=True, null=True)

    rly_unit = models.IntegerField(blank=True, null=True)

    appoint_date = models.DateField(blank=True, null=True)

    dt_retirement = models.DateField(blank=True, null=True)

    address = models.CharField(max_length=100, blank=True, null=True)

    pay_comm = models.CharField(max_length=2, blank=True, null=True)

    level = models.CharField(max_length=2, blank=True, null=True)

    pass_acc = models.CharField(max_length=10, blank=True, null=True)

    pass_entitled = models.CharField(max_length=3, blank=True, null=True)

    registered_by = models.CharField(max_length=14, blank=True, null=True)

    modified_by = models.CharField(max_length=14, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    registered_on = models.DateTimeField(blank=True, null=True)



    class Meta:

        db_table = 'comapp.comm_app_profile_retire'





class CommAppLogin(models.Model):

    login_id = models.CharField(primary_key=True, max_length=11)

    name = models.CharField(max_length=100, blank=True, null=True)

    desig_id = models.CharField(max_length=3, blank=True, null=True)

    dte_id = models.CharField(max_length=3, blank=True, null=True)

    bldg_id = models.CharField(max_length=3, blank=True, null=True)

    address = models.CharField(max_length=200, blank=True, null=True)

    mobno = models.CharField(max_length=10, blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)

    rly_ph_off = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    rly_ph_home = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    rly = models.CharField(max_length=4, blank=True, null=True)

    group = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    gaz_nongz = models.CharField(max_length=20, blank=True, null=True)

    registered_on = models.DateTimeField(blank=True, null=True)

    registered_by = models.CharField(max_length=11, blank=True, null=True)

    dsg_sname = models.CharField(max_length=60, blank=True, null=True)

    fname = models.CharField(max_length=60, blank=True, null=True)

    emp_dob = models.DateField(blank=True, null=True)

    marital_status = models.CharField(max_length=1, blank=True, null=True)

    emp_sex = models.CharField(max_length=1, blank=True, null=True)

    cur_basic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    grade_pay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    pay_band = models.CharField(max_length=5, blank=True, null=True)

    dt_retirement = models.DateField(blank=True, null=True)

    init_doa = models.DateField(blank=True, null=True)

    pay_level = models.CharField(max_length=10, blank=True, null=True)

    ctrl_officer = models.CharField(max_length=11, blank=True, null=True)

    pass_acct_no = models.CharField(max_length=10, blank=True, null=True)

    doa_rdso = models.DateField(blank=True, null=True)

    profile_verify_status = models.CharField(max_length=1, blank=True, null=True)

    family_verify_status = models.CharField(max_length=1, blank=True, null=True)



    class Meta:

        db_table = 'comm_app_login'





class CommAppLoginMaster(models.Model):

    ipasid = models.CharField(max_length=11, blank=True, null=True)

    password = models.CharField(max_length=50, blank=True, null=True)

    role = models.CharField(max_length=1, blank=True, null=True)

    emp_status = models.CharField(max_length=1, blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)

    active_flag = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    verified_by = models.CharField(max_length=50, blank=True, null=True)

    verified_on = models.DateTimeField(blank=True, null=True)

    estt_verify_status = models.CharField(max_length=1, blank=True, null=True)

    aadhar_no = models.CharField(max_length=12, blank=True, null=True)

    validupto_nonrdso = models.DateField(blank=True, null=True)

    rdso_nonrdso = models.SmallIntegerField(blank=True, null=True)

    otp = models.CharField(max_length=50, blank=True, null=True)

    rejection_reason = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_app_login_master'

        unique_together = (('ipasid', 'aadhar_no'),)





class CommAppLoginMaster1(models.Model):

    ipasid = models.CharField(max_length=11, blank=True, null=True)

    password = models.CharField(max_length=50, blank=True, null=True)

    role = models.CharField(max_length=1, blank=True, null=True)

    emp_status = models.CharField(max_length=1, blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)

    active_flag = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=11, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    verified_by = models.CharField(max_length=11, blank=True, null=True)

    verified_on = models.DateTimeField(blank=True, null=True)

    estt_verify_status = models.CharField(max_length=1, blank=True, null=True)

    aadhar_no = models.CharField(max_length=12, blank=True, null=True)

    validupto_nonrdso = models.DateField(blank=True, null=True)

    rdso_nonrdso = models.CharField(max_length=1, blank=True, null=True)



    class Meta:

        db_table = 'comm_app_login_master1'

        unique_together = (('ipasid', 'aadhar_no'), ('ipasid', 'aadhar_no'),)





class CommAppLoginMaster050719(models.Model):

    ipasid = models.CharField(max_length=11, blank=True, null=True)

    password = models.CharField(max_length=50, blank=True, null=True)

    role = models.CharField(max_length=1, blank=True, null=True)

    emp_status = models.CharField(max_length=1, blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)

    active_flag = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    verified_by = models.CharField(max_length=50, blank=True, null=True)

    verified_on = models.DateTimeField(blank=True, null=True)

    estt_verify_status = models.CharField(max_length=1, blank=True, null=True)

    aadhar_no = models.CharField(max_length=12, blank=True, null=True)

    validupto_nonrdso = models.DateField(blank=True, null=True)

    rdso_nonrdso = models.SmallIntegerField(blank=True, null=True)

    id = models.IntegerField(primary_key=True)

    otp = models.CharField(max_length=50, blank=True, null=True)

    rejection_reason = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_app_login_master_050719'





class CommAppLoginTrans(models.Model):

    login_id = models.CharField(max_length=11, blank=True, null=True)

    name = models.CharField(max_length=100, blank=True, null=True)

    desig_id = models.CharField(max_length=3, blank=True, null=True)

    dte_id = models.CharField(max_length=3, blank=True, null=True)

    bldg_id = models.CharField(max_length=3, blank=True, null=True)

    address = models.CharField(max_length=200, blank=True, null=True)

    mobno = models.CharField(max_length=10, blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)

    rly_ph_off = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    rly_ph_home = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    rly = models.CharField(max_length=4, blank=True, null=True)

    group = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    gaz_nongz = models.CharField(max_length=20, blank=True, null=True)

    registered_on = models.DateTimeField(blank=True, null=True)

    registered_by = models.CharField(max_length=11, blank=True, null=True)

    dsg_sname = models.CharField(max_length=60, blank=True, null=True)

    fname = models.CharField(max_length=60, blank=True, null=True)

    emp_dob = models.DateField(blank=True, null=True)

    marital_status = models.CharField(max_length=1, blank=True, null=True)

    emp_sex = models.CharField(max_length=1, blank=True, null=True)

    cur_basic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    grade_pay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    pay_band = models.CharField(max_length=5, blank=True, null=True)

    dt_retirement = models.DateField(blank=True, null=True)

    init_doa = models.DateField(blank=True, null=True)

    pay_level = models.CharField(max_length=10, blank=True, null=True)

    ctrl_officer = models.CharField(max_length=11, blank=True, null=True)

    pass_acct_no = models.CharField(max_length=10, blank=True, null=True)

    doa_rdso = models.DateField(blank=True, null=True)

    profile_verify_status = models.CharField(max_length=1, blank=True, null=True)

    family_verify_status = models.CharField(max_length=1, blank=True, null=True)



    class Meta:

        db_table = 'comm_app_login_trans'





class CommAppProfileNonrdso(models.Model):

    aadhar_no = models.CharField(primary_key=True, max_length=12)

    name = models.CharField(max_length=100, blank=True, null=True)

    dob = models.DateField(blank=True, null=True)

    fname = models.CharField(max_length=100, blank=True, null=True)

    email = models.CharField(max_length=100, blank=True, null=True)

    mobno = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    nodal_dte = models.CharField(max_length=2, blank=True, null=True)

    registered_on = models.DateField(blank=True, null=True)

    registered_by = models.CharField(max_length=12, blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)



    class Meta:

        db_table = 'comm_app_profile_nonrdso'





class CommApplicationMaster(models.Model):

    appid = models.IntegerField(primary_key=True)

    app_name = models.CharField(max_length=300, blank=True, null=True)

    app_link = models.CharField(max_length=300, blank=True, null=True)



    class Meta:

        db_table = 'comm_application_master'





class CommApplicationMaster1(models.Model):

    app_name = models.CharField(max_length=300, blank=True, null=True)

    app_link = models.CharField(max_length=300, blank=True, null=True)

    app_name1 = models.CharField(max_length=300, blank=True, null=True)

    app_link1 = models.CharField(max_length=300, blank=True, null=True)



    class Meta:

        db_table = 'comm_application_master_1'





class CommBldgMaster(models.Model):

    bldg_id = models.CharField(primary_key=True, max_length=2)

    bldg_desc = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_bldg_master'





class CommDeptMaster(models.Model):

    dept_id = models.CharField(primary_key=True, max_length=2)

    dept_desc = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_dept_master'





class CommDesigMaster(models.Model):

    desig_id = models.CharField(primary_key=True, max_length=3)

    desig_short = models.CharField(max_length=50)

    desig_desc = models.CharField(max_length=100)



    class Meta:

        db_table = 'comm_desig_master'





class CommDesigMasterOld(models.Model):

    desig_id = models.CharField(max_length=3)

    desig_desc = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_desig_master_old'





class CommDteMaster(models.Model):

    dte_id = models.CharField(primary_key=True, max_length=2)

    dte_desc = models.CharField(max_length=50, blank=True, null=True)

    billunit_desc = models.CharField(max_length=50, blank=True, null=True)

    short_desc = models.CharField(max_length=10, blank=True, null=True)

    vertical_dte = models.ForeignKey('CommVerticalDteMaster', models.DO_NOTHING, blank=True, null=True)



    class Meta:

        db_table = 'comm_dte_master'





class CommDteMasterOld(models.Model):

    dte_id = models.CharField(primary_key=True, max_length=2)

    dte_desc = models.CharField(max_length=50, blank=True, null=True)

    billunit_desc = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_dte_master_old'





class CommEmpFamily(models.Model):

    # idrow = models.AutoField(unique=True)

    ipas = models.CharField(primary_key=True, max_length=11)

    family_member_name = models.CharField(max_length=50)

    sex = models.CharField(max_length=1)

    dob = models.DateField()

    relation_code = models.CharField(max_length=2)

    active_flag = models.CharField(max_length=1)

    declaration_date = models.DateTimeField()

    entry_on = models.DateTimeField(blank=True, null=True)

    entry_by = models.CharField(max_length=11, blank=True, null=True)

    modified_by = models.CharField(max_length=11, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    member_index = models.BigIntegerField()



    class Meta:

        db_table = 'comm_emp_family'

        unique_together = (('ipas', 'member_index'),)





class CommEmpStatus(models.Model):

    status_code = models.CharField(primary_key=True, max_length=1)

    status_desc = models.CharField(max_length=20)



    class Meta:

        db_table = 'comm_emp_status'





class CommMenuMaster(models.Model):

    menu_id = models.IntegerField(blank=True, null=True)

    menu_name = models.CharField(max_length=100, blank=True, null=True)

    path = models.CharField(max_length=100, blank=True, null=True)

    lft = models.IntegerField(blank=True, null=True)

    rght = models.IntegerField(blank=True, null=True)

    title = models.CharField(max_length=100, blank=True, null=True)

    icon = models.CharField(max_length=50, blank=True, null=True)

    sort_order = models.CharField(max_length=10, blank=True, null=True)

    entry_by = models.CharField(max_length=11, blank=True, null=True)

    entry_on = models.DateTimeField(blank=True, null=True)

    modified_by = models.CharField(max_length=11, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)



    class Meta:

        db_table = 'comm_menu_master'


class ModelName(models.Model):
    auto_inc_id = models.IntegerField()


class CommNonrdsoAppPriv(models.Model):

    id = models.IntegerField()

    aadhar_no = models.CharField(primary_key=True, max_length=12)

    appid = models.IntegerField()

    flag = models.CharField(max_length=1, blank=True, null=True)

    entry_by = models.CharField(max_length=50, blank=True, null=True)

    entry_on = models.DateTimeField(blank=True, null=True)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)



    class Meta:

        db_table = 'comm_nonrdso_app_priv'

        unique_together = (('aadhar_no', 'appid'),)





class CommPayLevel(models.Model):

    level_srt = models.CharField(max_length=5)

    level_desc = models.CharField(max_length=10, blank=True, null=True)

    gradelevel = models.CharField(max_length=5, blank=True, null=True)



    class Meta:

        db_table = 'comm_pay_level'





class CommRelationMaster(models.Model):

    relation_code = models.CharField(primary_key=True, max_length=2)

    relation_desc = models.CharField(max_length=30, blank=True, null=True)



    class Meta:

        db_table = 'comm_relation_master'





class CommRoleMaster(models.Model):

    role_id = models.IntegerField(blank=True, null=True)

    role_name = models.CharField(max_length=30, blank=True, null=True)

    lft = models.IntegerField(blank=True, null=True)

    rght = models.IntegerField(blank=True, null=True)

    entry_by = models.CharField(max_length=11, blank=True, null=True)

    entry_on = models.DateTimeField(blank=True, null=True)

    modified_by = models.CharField(max_length=11, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    sort_order = models.CharField(max_length=10, blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)



    class Meta:

        db_table = 'comm_role_master'





class CommRolePriv(models.Model):

    role_id = models.IntegerField(primary_key=True)

    menu_id = models.IntegerField()

    entry_by = models.CharField(max_length=11, blank=True, null=True)

    entry_on = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=1, blank=True, null=True)

    modified_by = models.CharField(max_length=11, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)



    class Meta:

        db_table = 'comm_role_priv'

        unique_together = (('role_id', 'menu_id'),)





class CommUsertypeMaster(models.Model):

    user_type = models.AutoField(primary_key=True)

    type_desc = models.CharField(max_length=20, blank=True, null=True)



    class Meta:

        db_table = 'comm_usertype_master'





class CommVerifyRole(models.Model):

    ipasid = models.CharField(max_length=11, blank=True, null=True)

    dte_id = models.CharField(max_length=3)

    activeflag = models.CharField(max_length=1)

    modified_by = models.CharField(max_length=50, blank=True, null=True)

    modified_on = models.DateTimeField(blank=True, null=True)

    email = models.CharField(max_length=50, blank=True, null=True)



    class Meta:

        db_table = 'comm_verify_role'

        unique_together = (('ipasid', 'dte_id', 'email'),)





class CommVerticalDteMaster(models.Model):

    vertical_dte_id = models.SmallIntegerField(primary_key=True)

    vertical_desc = models.CharField(max_length=100)

    vertical_sort = models.CharField(max_length=50)

    vertical_head = models.CharField(max_length=20)



    class Meta:

        db_table = 'comm_vertical_dte_master'





class EmpVisitDetails(models.Model):

    emp_no = models.CharField(max_length=11, blank=True, null=True)

    last_visit_on = models.DateTimeField(blank=True, null=True)

    emp_visit_no = models.IntegerField(blank=True, null=True)

    total_visits_no = models.IntegerField(blank=True, null=True)

    emp_ip_address = models.CharField(max_length=15, blank=True, null=True)



    class Meta:

        db_table = 'emp_visit_details'





class PayBandMaster(models.Model):

    pay_band = models.CharField(max_length=5, blank=True, null=True)

    pay_band_scale = models.CharField(primary_key=True, max_length=11)

    grade_pay = models.IntegerField()



    class Meta:

        db_table = 'pay_band_master'

        unique_together = (('pay_band_scale', 'grade_pay'),)





class ViicpcFixationMatrix(models.Model):

    increment_srno = models.BigIntegerField(blank=True, null=True)

    l_1 = models.BigIntegerField(blank=True, null=True)

    l_2 = models.BigIntegerField(blank=True, null=True)

    l_3 = models.BigIntegerField(blank=True, null=True)

    l_4 = models.BigIntegerField(blank=True, null=True)

    l_5 = models.BigIntegerField(blank=True, null=True)

    l_6 = models.BigIntegerField(blank=True, null=True)

    l_7 = models.BigIntegerField(blank=True, null=True)

    l_8 = models.BigIntegerField(blank=True, null=True)

    l_9 = models.BigIntegerField(blank=True, null=True)

    l_10 = models.BigIntegerField(blank=True, null=True)

    l_11 = models.BigIntegerField(blank=True, null=True)

    l_12 = models.BigIntegerField(blank=True, null=True)

    l_13 = models.BigIntegerField(blank=True, null=True)

    l_13a = models.BigIntegerField(blank=True, null=True)

    l_14 = models.BigIntegerField(blank=True, null=True)

    l_15 = models.BigIntegerField(blank=True, null=True)

    l_16 = models.BigIntegerField(blank=True, null=True)

    l_17 = models.BigIntegerField(blank=True, null=True)

    l_18 = models.BigIntegerField(blank=True, null=True)



    class Meta:

        db_table = 'viicpc_fixation_matrix'


class Empdetail(models.Model):
    login_id = models.CharField(max_length=11, blank=True, null=False,primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    desig_id = models.CharField(max_length=3, blank=True, null=True)
    desig_desc = models.CharField(max_length=100, blank=True, null=True)
    bldg_id = models.CharField(max_length=3, blank=True, null=True)
    bldg_desc = models.CharField(max_length=50, blank=True, null=True)
    dte_id = models.CharField(max_length=3, blank=True, null=True)
    dte_desc = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobno = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    rly_ph_off = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rly_ph_home = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rly = models.CharField(max_length=4, blank=True, null=True)
    group = models.CharField(max_length=1, blank=True, null=True)
    gaz_nongz = models.CharField(max_length=20, blank=True, null=True)
    emp_sex = models.CharField(max_length=1, blank=True, null=True)
    fname = models.CharField(max_length=60, blank=True, null=True)
    emp_dob = models.DateField(blank=True, null=True)
    marital_status = models.CharField(max_length=1, blank=True, null=True)
    cur_basic = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    grade_pay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dt_retirement = models.DateField(blank=True, null=True)
    init_doa = models.DateField(blank=True, null=True)
    pay_level = models.CharField(max_length=10, blank=True, null=True)
    pass_acct_no = models.CharField(max_length=10, blank=True, null=True)
    doa_rdso = models.DateField(blank=True, null=True)
    desig_short = models.CharField(max_length=50, blank=True, null=True)
    billunit_desc = models.CharField(max_length=50, blank=True, null=True)
    family_verify_status = models.CharField(max_length=1, blank=True, null=True)
    profile_verify_status = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.CharField(max_length=1, blank=True, null=True)
    dte_short_desc = models.CharField(max_length=10, blank=True, null=True)
    rdso_nonrdso = models.SmallIntegerField(blank=True, null=True)
    aadhar_no = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'empdetail'

class AmcFirmMaster(models.Model):
    firm_id = models.SmallIntegerField(primary_key=True)
    firm_name = models.CharField(max_length=60, blank=True, null=True)
    directorate_id = models.CharField(max_length=2, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    contract_no = models.CharField(max_length=80, blank=True, null=True)
    entry_by = models.CharField(max_length=11, blank=True, null=True)
    entry_on = models.DateTimeField(blank=True, null=True)
    modify_by = models.CharField(max_length=11, blank=True, null=True)
    modify_on = models.DateTimeField(blank=True, null=True)
    amc_start_from = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amc_firm_master'


class ComplaintAreaCategory(models.Model):
    directorate_id = models.CharField(primary_key=True, max_length=2)
    complaint_category_id = models.SmallIntegerField()
    complaint_category = models.CharField(max_length=100, blank=True, null=True)
    type_id = models.CharField(max_length=2, blank=True, null=True)
    sub_dir_id = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_area_category'
        unique_together = (('directorate_id', 'complaint_category_id'),)


class ComplaintDirectorate(models.Model):
    directorate_id = models.CharField(primary_key=True, max_length=2)
    directorate_name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_directorate'


class ComplaintForemanTeam(models.Model):
    directorate_id = models.CharField(primary_key=True, max_length=2)
    member_id = models.SmallIntegerField()
    member_name = models.CharField(max_length=85, blank=True, null=True)
    sub_dir_id = models.CharField(max_length=3, blank=True, null=True)
    isactive = models.SmallIntegerField(blank=True, null=True)
    vender_id = models.SmallIntegerField(blank=True, null=True)
    entry_by = models.CharField(max_length=11, blank=True, null=True)
    entry_on = models.DateTimeField(blank=True, null=True)
    modify_by = models.CharField(max_length=11, blank=True, null=True)
    modify_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_foreman_team'
        unique_together = (('directorate_id', 'member_id'),)


class ComplaintMenuMaster(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_name = models.CharField(max_length=100)
    path = models.CharField(max_length=100, blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_menu_master'
        unique_together = (('menu_id', 'menu_name'),)


class ComplaintRegistration(models.Model):
    id = models.IntegerField(blank=True, null=True)
    complaint_no = models.CharField(max_length=15, blank=True, null=True)
    complaint_id = models.IntegerField(primary_key=True)
    complaint_type_id = models.CharField(max_length=1, blank=True, null=True)
    qtr_no_or_building_id = models.CharField(max_length=11, blank=True, null=True)
    qtr_type_code_or_directorate = models.CharField(max_length=3, blank=True, null=True)
    complaint_category_id = models.IntegerField(blank=True, null=True)
    complaint_description = models.CharField(max_length=300, blank=True, null=True)
    status_flag = models.CharField(max_length=2, blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    directorate = models.ForeignKey(ComplaintForemanTeam, models.DO_NOTHING, blank=True, null=True)
    foreman_description = models.CharField(max_length=100, blank=True, null=True)
    machine_serial_no = models.CharField(max_length=20, blank=True, null=True)
    amc_firm_id = models.SmallIntegerField(blank=True, null=True)
    sub_dir_id = models.CharField(max_length=3, blank=True, null=True)
    pf_no = models.CharField(max_length=11, blank=True, null=True)
    alloted_by = models.CharField(max_length=12, blank=True, null=True)
    complaint_date = models.DateField(blank=True, null=True)
    complaint_time = models.TimeField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    completion_time = models.TimeField(blank=True, null=True)
    modified_by_foreman = models.CharField(max_length=11, blank=True, null=True)
    modified_on_foreman = models.DateTimeField(blank=True, null=True)
    entry_on_foreman = models.DateTimeField(blank=True, null=True)
    escalated = models.CharField(max_length=1, blank=True, null=True)
    verified_by = models.CharField(max_length=11, blank=True, null=True)
    verified_on = models.DateTimeField(blank=True, null=True)
    first_time_attended_by = models.CharField(max_length=12, blank=True, null=True)
    first_time_attended_on = models.DateTimeField(blank=True, null=True)
    first_time_status_flag = models.CharField(max_length=2, blank=True, null=True)
    long_term_option = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_registration'


class ComplaintRoleMaster(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=30, blank=True, null=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_role_master'


class ComplaintRolePriv(models.Model):
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_role_priv'


class ComplaintSubDirectorate(models.Model):
    sub_dir_id = models.CharField(primary_key=True, max_length=3)
    sub_dir_name = models.CharField(max_length=20, blank=True, null=True)
    directorate_id = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_sub_directorate'


class ComplaintUserRole(models.Model):
    user_id = models.CharField(max_length=12, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    entry_by = models.CharField(max_length=11, blank=True, null=True)
    modified_by = models.CharField(max_length=11, blank=True, null=True)
    entry_on = models.DateTimeField(blank=True, null=True)
    modified_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    directorate_id = models.CharField(max_length=2, blank=True, null=True)
    sub_dir_id = models.CharField(max_length=3, blank=True, null=True)
    firm_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_user_role'


class EscalatedComplaints(models.Model):
    escalated_on = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    attended_by = models.CharField(max_length=11, blank=True, null=True)
    reason_for_escalation = models.CharField(max_length=100, blank=True, null=True)
    complaint_no = models.CharField(primary_key=True, max_length=15)
    remarks_by_foreman = models.CharField(max_length=100, blank=True, null=True)
    attended_on = models.DateField(blank=True, null=True)
    attended_time = models.TimeField(blank=True, null=True)
    attended_by_foreman_date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalated_complaints'


class MachineAmcDetails(models.Model):
    record_id = models.IntegerField(primary_key=True)
    machine_unique_id = models.CharField(max_length=9)
    inclusion_finalized_by = models.CharField(max_length=11, blank=True, null=True)
    inclusion_finalized_on = models.DateTimeField(blank=True, null=True)
    firm_id = models.SmallIntegerField(blank=True, null=True)
    accept_or_reject_by_admin = models.CharField(max_length=1, blank=True, null=True)
    remarks_by_admin = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_amc_details'


class MachineDirectorate(models.Model):
    directorate_name = models.CharField(max_length=30, blank=True, null=True)
    dir_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_directorate'


class MachineEmpMaster(models.Model):
    machine_unique_id = models.CharField(primary_key=True, max_length=9)
    machine_type = models.CharField(max_length=2, blank=True, null=True)
    machine_alloted_to = models.CharField(max_length=11, blank=True, null=True)
    machine_alloted_by = models.CharField(max_length=11, blank=True, null=True)
    machine_alloted_on = models.DateTimeField(blank=True, null=True)
    machine_allocation_remarks = models.CharField(max_length=50, blank=True, null=True)
    firm_id = models.SmallIntegerField(blank=True, null=True)
    last_modified_on = models.DateTimeField(blank=True, null=True)
    last_modified_by = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_emp_master'


class MachineTypeMaster(models.Model):
    type_id = models.CharField(max_length=2, blank=True, null=True)
    type_description = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_type_master'


class QtrMaster(models.Model):
    qtr_no = models.CharField(primary_key=True, max_length=11)
    sector = models.CharField(max_length=3, blank=True, null=True)
    status_code = models.CharField(max_length=2, blank=True, null=True)
    floor = models.SmallIntegerField(blank=True, null=True)
    colony = models.CharField(max_length=1, blank=True, null=True)
    lawn = models.CharField(max_length=1, blank=True, null=True)
    pool_code = models.CharField(max_length=4, blank=True, null=True)
    type_code = models.CharField(max_length=2, blank=True, null=True)
    servent_qtr = models.SmallIntegerField(blank=True, null=True)
    garage = models.SmallIntegerField(blank=True, null=True)
    plinth_area_code = models.SmallIntegerField(blank=True, null=True)
    status_date = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=4, blank=True, null=True)
    pf_no = models.IntegerField(blank=True, null=True)
    under_repair_flag = models.CharField(max_length=1, blank=True, null=True)
    transfer_to = models.CharField(max_length=4, blank=True, null=True)
    book_flag = models.CharField(max_length=1, blank=True, null=True)
    rent_type = models.CharField(max_length=1, blank=True, null=True)
    entry_by = models.CharField(max_length=10, blank=True, null=True)
    entry_on = models.DateField(blank=True, null=True)
    modified_by = models.CharField(max_length=10, blank=True, null=True)
    modified_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qtr_master'


class QtrType(models.Model):
    qtr_type = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'qtr_type'


class Sector(models.Model):
    sector = models.CharField(primary_key=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'sector'
        

class ComplainCasetypeMaster(models.Model):
    directorate = models.ForeignKey('ComplaintDirectorate', models.DO_NOTHING)
    complain_type = models.CharField(max_length=20)
    type_id = models.CharField(max_length=3)
    sno_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'complain_casetype_master'