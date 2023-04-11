# Generated by Django 4.2 on 2023-04-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0011_alter_author_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="language",
            field=models.CharField(
                choices=[
                    ("NOT SET", "Not set"),
                    ("KӀАХЭ", "Адыгабзэ"),
                    ("ЩХЬАГЪ", "Адыгэбзэ"),
                ],
                default="NOT SET",
                max_length=20,
                verbose_name="Language",
            ),
        ),
    ]
