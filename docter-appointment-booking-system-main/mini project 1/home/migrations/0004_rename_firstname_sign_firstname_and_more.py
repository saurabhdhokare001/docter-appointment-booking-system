# Generated by Django 5.1.1 on 2024-10-19 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_delete_signup_alter_sign_firstname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sign",
            old_name="FirstName",
            new_name="firstName",
        ),
        migrations.RenameField(
            model_name="sign",
            old_name="LastName",
            new_name="lastName",
        ),
    ]
