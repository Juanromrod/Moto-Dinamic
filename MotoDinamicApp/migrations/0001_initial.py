# Generated by Django 4.0.3 on 2022-05-24 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=128)),
                ('direccion', models.CharField(max_length=128)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=30, unique=True)),
                ('color', models.CharField(max_length=30)),
                ('kilometraje', models.IntegerField()),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='motos')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_problema', models.CharField(max_length=228)),
                ('fecha_ingreso', models.DateTimeField()),
                ('info_adicional', models.CharField(max_length=228)),
                ('idCliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.cliente')),
                ('idMoto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.moto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('desc', models.CharField(max_length=128)),
                ('idTipoServicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.tiposervicio')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('desc', models.CharField(max_length=128)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('idTipoProducto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeIngreso_Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idOrdenDeIngreso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.ordendeingreso')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Factura_Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFactura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.factura')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Factura_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('idFactura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.factura')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente_Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.cliente')),
                ('idFactura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MotoDinamicApp.factura')),
            ],
        ),
    ]
