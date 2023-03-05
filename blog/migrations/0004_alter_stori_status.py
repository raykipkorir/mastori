# Generated by Django 4.1.3 on 2023-02-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_stori_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stori",
            name="status",
            field=models.CharField(
                choices=[("draft", "draft"), ("published", "published")],
                default="draft",
                max_length=20,
            ),
        ),
    ]