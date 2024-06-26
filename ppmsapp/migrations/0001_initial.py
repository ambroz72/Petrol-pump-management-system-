# Generated by Django 4.1.3 on 2022-11-18 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=100, null=True)),
                ('product_price', models.IntegerField(null=True)),
                ('product_stock', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_fname', models.CharField(max_length=30, null=True)),
                ('e_lname', models.CharField(max_length=30, null=True)),
                ('e_address', models.CharField(max_length=100, null=True)),
                ('e_gender', models.CharField(max_length=100, null=True)),
                ('e_age', models.IntegerField(null=True)),
                ('e_phone_numbr', models.BigIntegerField(null=True, verbose_name=10)),
                ('e_email', models.EmailField(max_length=254, null=True)),
                ('e_post', models.CharField(max_length=20, null=True)),
                ('e_photo', models.ImageField(null=True, upload_to='image/')),
                ('e_shift', models.CharField(max_length=30, null=True)),
                ('e_status', models.CharField(max_length=10, null=True)),
                ('e_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmsapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=60)),
                ('r_DOB', models.DateField(null=True)),
                ('r_details', models.CharField(max_length=500, null=True)),
                ('r_quantity', models.IntegerField(null=True)),
                ('r_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmsapp.category')),
                ('r_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_req', models.CharField(max_length=50, null=True)),
                ('l_reason', models.CharField(max_length=100)),
                ('l_DOB', models.DateField()),
                ('l_status', models.CharField(max_length=10, null=True)),
                ('l_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('l_users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmsapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50, null=True)),
                ('f_feed', models.CharField(max_length=100)),
                ('f_DOB', models.DateField(null=True)),
                ('f_status', models.CharField(max_length=10, null=True)),
                ('f_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('f_users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmsapp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='e_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ppmsapp.report'),
        ),
        migrations.AddField(
            model_name='employee',
            name='e_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_attendnce', models.CharField(max_length=30, null=True)),
                ('a_DOB', models.DateField(null=True)),
                ('a_post', models.CharField(max_length=30, null=True)),
                ('a_shift', models.CharField(max_length=30, null=True)),
                ('a_status', models.CharField(max_length=10, null=True)),
                ('a_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('a_users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ppmsapp.employee')),
            ],
        ),
    ]
