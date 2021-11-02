# Generated by Django 3.2.7 on 2021-11-02 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('short_desc', models.TextField(null=True)),
                ('long_desc', models.TextField(null=True)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('sku', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
