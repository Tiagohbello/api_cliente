# Generated by Django 4.0.1 on 2022-01-06 21:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.IntegerField()),
                ('data_nascimento', models.DateField(max_length=255)),
                ('data_cliente', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
