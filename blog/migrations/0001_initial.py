# Generated by Django 5.1.4 on 2025-02-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('head0', models.CharField(default='', max_length=5000)),
                ('contenthead', models.TextField(default='', max_length=5000)),
                ('head1', models.CharField(max_length=100)),
                ('contenthead1', models.TextField(default='', max_length=500)),
                ('head2', models.CharField(max_length=100)),
                ('contenthead2', models.TextField(default='', max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
