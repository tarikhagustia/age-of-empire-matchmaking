# Generated by Django 5.0.6 on 2024-07-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalApp', '0002_tblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPlayerGameMatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl_match_id', models.IntegerField(null=True)),
                ('cl_player_id', models.IntegerField(null=True)),
                ('cl_match_result', models.IntegerField(null=True)),
                ('cl_started_at', models.DateTimeField(null=True)),
                ('cl_finished_at', models.DateTimeField(null=True)),
                ('cl_status', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='TbGameMatches',
        ),
        migrations.RemoveField(
            model_name='tbmember',
            name='fk_group',
        ),
        migrations.DeleteModel(
            name='TbMatchTeam',
        ),
        migrations.RenameField(
            model_name='tbplayer',
            old_name='cl_drops',
            new_name='cl_win_streak',
        ),
        migrations.RemoveField(
            model_name='tbmember',
            name='fk_player',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_aoe_version',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_elo',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_elo_1vs1',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_elo_team',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_elo_unranked',
        ),
        migrations.RemoveField(
            model_name='tbplayer',
            name='cl_streak',
        ),
        migrations.AddField(
            model_name='tbplayer',
            name='cl_player_id',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='TbGroup',
        ),
    ]
