# Generated by Django 5.0.4 on 2024-04-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fanmavzusi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('test_soni', models.IntegerField(help_text="o'qivchi qancha test yechadi !! masalan: 20 yoki 25 yoki 62 istalgan")),
                ('vaqti', models.IntegerField(help_text="Qancha Minit bo'lishini Kirgazing!! ")),
                ('utish_foizi', models.IntegerField(help_text="o'tish foizini kiriting!!")),
                ('tur', models.CharField(choices=[('BOSH', 'bolshlangich 8 yoshdan 12 atrofdagi bolalarga '), ('ORTA', "o'rtacha  13 yoshdan 17 atrofdagi bolalarga "), ('MRAK', 'murakkab  18 yoshdan + atrofdagi bolalarga ')], max_length=20)),
            ],
        ),
    ]
