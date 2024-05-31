# Generated by Django 2.1 on 2024-05-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bum_tester', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('document_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bum_tester.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('document_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='pair',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bum_tester.Question'),
        ),
    ]