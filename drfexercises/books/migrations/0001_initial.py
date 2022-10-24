# Generated by Django 4.1.2 on 2022-10-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=12)),
                ('etag', models.CharField(max_length=11)),
                ('title', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('categories', models.TextField(null=True)),
                ('average_rating', models.IntegerField(null=True)),
                ('ratings_count', models.IntegerField(null=True)),
                ('thumbnail', models.CharField(max_length=100, null=True)),
                ('authors', models.ManyToManyField(related_name='authors', to='books.author')),
            ],
        ),
    ]
