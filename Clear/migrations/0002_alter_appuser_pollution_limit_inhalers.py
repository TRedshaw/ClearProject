# Generated by Django 4.1.4 on 2023-01-07 22:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clear', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='pollution_limit',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.CreateModel(
            name='Inhalers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhaler_type', models.CharField(choices=[('Beclametasone_dipropionate', 'Beclametasone_dipropionate'), ('Ciclesonide', 'Ciclesonide'), ('Fluticasone_poprionate', 'Fluticasone_poprionate'), ('Beclometasone', 'Beclometasone'), ('Budesonide', 'Budesonide'), ('Fluticasone_poprionate', 'Fluticasone_poprionate'), ('Mometasone', 'Mometasone'), ('Beclometasone_dipropionate_with_ormoterol', 'Beclometasone_dipropionate_with_ormoterol'), ('Budesonid_with_formoterol', 'Budesonid_with_formoterol'), ('Fluticasone_poprionate_with_formoterol', 'Fluticasone_poprionate_with_formoterol'), ('Fluticasone_poprionate_with_salmeterol', 'Fluticasone_poprionate_with_salmeterol'), ('Fluticasone_furoate_with_vilanterol', 'Fluticasone_furoate_with_vilanterol')], max_length=200)),
                ('puffs_remaining', models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30'), ('40', '40'), ('50', '50'), ('60', '60'), ('70', '70'), ('80', '80'), ('90', '90'), ('100', '100')], max_length=20)),
                ('puffs', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=200)),
                ('per_Day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inhaler_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]