# Generated by Django 4.2.7 on 2024-02-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_customuser_click_on_link1_customuser_click_on_link2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='invite_link',
            field=models.CharField(default='d6187709090d4cd2a8e5d2fdadd27c14', max_length=50),
        ),
    ]