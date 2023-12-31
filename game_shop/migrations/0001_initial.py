from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='games')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='game_shop.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
