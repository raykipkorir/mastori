# Generated by Django 4.1.3 on 2023-04-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_stori_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="user",
            new_name="account",
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="Post_id",
            new_name="post",
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]