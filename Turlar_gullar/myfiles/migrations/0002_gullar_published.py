# Generated by Django 5.1.2 on 2024-12-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gullar',
            name='published',
            field=models.BooleanField(default=True, help_text="Belgilangan bo'lsa, saytga chiqaradi!", verbose_name='Saytga chiqarish'),
        ),
    ]