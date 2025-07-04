# Generated by Django 5.2 on 2025-04-24 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_subcategories_category'),
        ('user', '0004_temporaryuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ManyToManyField(blank=True, related_name='orders', to='shop.product')),
                ('temp_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.temporaryuser')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.CheckConstraint(condition=models.Q(models.Q(('user__isnull', False), ('temp_user__isnull', True)), models.Q(('user__isnull', True), ('temp_user__isnull', False)), _connector='OR'), name='one_of_user_must_be_passed')],
            },
        ),
    ]
