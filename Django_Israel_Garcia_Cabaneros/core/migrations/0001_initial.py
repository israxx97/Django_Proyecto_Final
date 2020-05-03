# Generated by Django 3.0.4 on 2020-04-30 08:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodega', models.CharField(help_text='Introduce una nueva bodega.', max_length=70, verbose_name='Bodega')),
                ('imagen', models.ImageField(blank=True, help_text='Introduce la imagen corporativa de la bodega.', null=True, upload_to='bodegas', verbose_name='Imagen')),
                ('created', models.DateField(auto_now_add=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de última actualización')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Introduce un nuevo tipo de vino.', max_length=40, verbose_name='Tipo')),
                ('created', models.DateField(auto_now_add=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de última actualización')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Vino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introduce un nombre.', max_length=50, verbose_name='Nombre')),
                ('anyo', models.CharField(choices=[('1950', '1950'), ('1951', '1951'), ('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020')], help_text='Selecciona un año.', max_length=4, verbose_name='Año')),
                ('denominacion', models.CharField(help_text='Lugar de procedencia del producto.', max_length=100, verbose_name='Denominación de Origen')),
                ('volumen', models.PositiveIntegerField(help_text='Campo entero positivo.', verbose_name='Volumen (cL)')),
                ('stock', models.PositiveIntegerField(help_text='Campo entero positivo.', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stock')),
                ('ventas_totales', models.PositiveIntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Unidades vendidas')),
                ('descripcion', models.TextField(help_text='Introduce una descripción del producto.', max_length=1000, verbose_name='Descripción')),
                ('imagen', models.ImageField(blank=True, help_text='Introduce una imagen del vino a mostrar.', null=True, upload_to='vinos', verbose_name='Imagen')),
                ('precio', models.FloatField()),
                ('created', models.DateField(auto_now_add=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, help_text='Este campo se introducirá automáticamente.', verbose_name='Fecha de última actualización')),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bodega', verbose_name='Bodega')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Vino',
                'verbose_name_plural': 'Vinos',
                'ordering': ['stock'],
            },
        ),
    ]
