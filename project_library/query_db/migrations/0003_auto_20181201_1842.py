# Generated by Django 2.1.3 on 2018-12-01 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query_db', '0002_auto_20180928_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tb_authors',
            },
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='query_db.AuthorInfo'),
            preserve_default=False,
        ),
    ]
