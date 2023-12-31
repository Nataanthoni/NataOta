# Generated by Django 4.2.7 on 2023-11-09 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('NA', 'National Newspaper'), ('IN', 'International Newspaper'), ('RN', 'Regional Newspaper'), ('JM', 'Journal/Magazine'), ('OT', 'Others')], default='NA', max_length=2)),
                ('o_type', models.CharField(choices=[('FR', 'Free Newspaper'), ('PD', 'Paid Newspaper'), ('OT', 'Others')], default='FR', max_length=2)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(default='password0', max_length=200)),
                ('confirm_password', models.CharField(default='password0', max_length=200)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('no_of_newspapers', models.CharField(max_length=200)),
                ('added_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
        ),
    ]
