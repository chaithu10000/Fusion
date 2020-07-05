# Generated by Django 3.0.7 on 2020-06-29 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('globals', '0003_auto_20191024_1242'),
        ('establishment', '0005_auto_20200603_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ltc_application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('adjustments_pending', 'Adjustments Pending'), ('finished', 'Finished')], max_length=20, null=True)),
                ('pf_number', models.CharField(default='', max_length=50)),
                ('basic_pay', models.IntegerField(blank=True)),
                ('is_leave_required', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=50)),
                ('leave_start', models.DateField()),
                ('leave_end', models.DateField()),
                ('family_departure_date', models.DateField()),
                ('leave_nature', models.CharField(default='', max_length=50)),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('is_hometown_or_elsewhere', models.CharField(choices=[('hometown', 'Home Town'), ('elsewhere', 'Elsewhere')], max_length=50)),
                ('phone_number', models.CharField(default='', max_length=13)),
                ('address_during_leave', models.CharField(blank=True, default='', max_length=500)),
                ('travel_mode', models.CharField(choices=[('rail', 'Rail'), ('road', 'Road')], max_length=50)),
                ('ltc_availed', models.CharField(blank=True, default='', max_length=100)),
                ('ltc_to_avail', models.CharField(blank=True, default='', max_length=200)),
                ('dependents', models.CharField(blank=True, default='', max_length=500)),
                ('requested_advance', models.IntegerField(blank=True)),
                ('request_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('review_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Ltc Application',
            },
        ),
        migrations.CreateModel(
            name='Ltc_eligible_user',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_joining', models.DateField(default='2005-04-01')),
                ('current_block_size', models.IntegerField(default=4)),
                ('total_ltc_allowed', models.IntegerField(default=2)),
                ('hometown_ltc_allowed', models.IntegerField(default=1)),
                ('elsewhere_ltc_allowed', models.IntegerField(default=1)),
                ('hometown_ltc_availed', models.IntegerField(default=0)),
                ('elsewhere_ltc_availed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ltc_tracking',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tracking_info', serialize=False, to='establishment.Ltc_application')),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('review_status', models.CharField(choices=[('to_assign', 'To Assign'), ('under_review', 'Under Review'), ('reviewed', 'Reviewed')], max_length=20, null=True)),
                ('reviewer_design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.Designation')),
                ('reviewer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Ltc Tracking',
            },
        ),
    ]
