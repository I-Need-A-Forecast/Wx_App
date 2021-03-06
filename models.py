# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Meteorologist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_information = models.ForeignKey('UserInformation', models.DO_NOTHING, db_column='User_Information_ID')  # Field name made lowercase.
    actual_name = models.CharField(db_column='Actual Name', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    screen_name = models.CharField(db_column='Screen Name', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_display_toggle = models.IntegerField(db_column='Name Display Toggle')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address = models.CharField(db_column='Email Address', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mailing_address = models.CharField(db_column='Mailing Address', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_address = models.CharField(db_column='Billing Address', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone Number', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_creation_date = models.DateField(db_column='Account Creation Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    personal_biography = models.TextField(db_column='Personal Biography')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_information = models.CharField(db_column='Payment Information', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_score = models.IntegerField(db_column='Current Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_flag = models.IntegerField(db_column='User Flag')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lockout_date = models.CharField(db_column='Lockout Date', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'meteorologist'
        unique_together = (('id', 'user_information'),)


class UserInformation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    first_name = models.TextField(db_column='First_Name')  # Field name made lowercase.
    last_name = models.TextField(db_column='Last_Name')  # Field name made lowercase.
    display_first_letter_last_name = models.IntegerField(db_column='Display_First_Letter_Last_Name')  # Field name made lowercase.
    screen_name = models.CharField(db_column='Screen_Name', max_length=16, blank=True, null=True)  # Field name made lowercase.
    display_screen_name = models.IntegerField(db_column='Display_Screen_Name')  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=255)  # Field name made lowercase.
    address_ordinal = models.IntegerField(db_column='Address_Ordinal')  # Field name made lowercase.
    primary = models.IntegerField(db_column='Primary')  # Field name made lowercase.
    address_1 = models.CharField(db_column='Address_1', max_length=255)  # Field name made lowercase.
    address_2 = models.CharField(db_column='Address_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255)  # Field name made lowercase.
    state_province = models.CharField(db_column='State_Province', max_length=255)  # Field name made lowercase.
    zip_code = models.CharField(db_column='Zip_Code', max_length=10)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.
    billing_address_1 = models.CharField(db_column='Billing_Address_1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billing_address_2 = models.CharField(db_column='Billing_Address_2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billing_city = models.CharField(db_column='Billing_City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billing_state_province = models.CharField(db_column='Billing_State_Province', max_length=255, blank=True, null=True)  # Field name made lowercase.
    billing_zip_code = models.CharField(db_column='Billing_Zip_Code', max_length=45, blank=True, null=True)  # Field name made lowercase.
    billing_country = models.CharField(db_column='Billing_Country', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_information'
