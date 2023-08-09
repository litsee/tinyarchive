# Generated by Django 4.0.5 on 2022-06-23 18:26

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('photo_image', stdimage.models.StdImageField(force_min_size=False, upload_to='photographs/', variations={'thumbnail': {'height': 300, 'width': 300}})),
            ],
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='id',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='name',
        ),
        migrations.RemoveField(
            model_name='photograph',
            name='photo_image',
        ),
        migrations.AddField(
            model_name='photograph',
            name='type',
            field=models.CharField(choices=[('glass', 'Glass Slide'), ('35mm', '35mm Slide'), ('polaroid', 'Polaroid'), ('print', 'Printed Photo'), ('digital', 'Born Digital Photo')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('archivedocument_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.archivedocument')),
            ],
            bases=('archive.archivedocument',),
        ),
        migrations.AddField(
            model_name='photograph',
            name='archivedocument_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='archive.archivedocument'),
            preserve_default=False,
        ),
    ]
