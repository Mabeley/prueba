# Generated by Django 4.0.4 on 2022-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=45, unique=True)),
                ('password', models.TextField()),
                ('numero_cel', models.CharField(max_length=45)),
                ('rol', models.CharField(choices=[['ADMINISTRATOR', 'ADMINISTRADOR'], ['USER', 'USUARIO']], max_length=40)),
                ('codigo_activacion', models.CharField(max_length=6)),
                ('fecha_vence_plan', models.CharField(max_length=45)),
                ('formato_impresion', models.CharField(choices=[['80mm', '80mm'], ['57mm', '57mm']], max_length=20)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]