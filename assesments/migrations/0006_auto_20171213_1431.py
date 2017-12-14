# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-13 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assesments', '0005_auto_20171213_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='brief_answer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='correct_options',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='max_marks',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option_five',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option_four',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option_one',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option_three',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='option_two',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question_slug',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question_text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question_type',
        ),
        migrations.AddField(
            model_name='answer',
            name='for_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='assesments.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='total_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='total_question',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='written_answer',
            field=models.TextField(),
        ),
    ]