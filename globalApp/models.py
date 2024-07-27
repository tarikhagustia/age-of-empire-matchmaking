from django.db import models

# Create your models here.
class TbPlayer(models.Model):
    cl_aoe_version = models.CharField(max_length = 100, null=True)
    cl_player_name = models.CharField(max_length = 100, null=True)
    cl_avatar_url = models.CharField(max_length = 200, null=True)
    cl_player_alias = models.CharField(max_length = 100, null=True)
    cl_player_alias = models.CharField(max_length = 100, null = True)
    cl_elo_unranked = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_elo_1vs1 = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_elo_team = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_drops = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_streak = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_last_win_count = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_last_lose_count = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_elo =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_final_elo = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    

class TbGroup(models.Model):
    cl_groupname = models.CharField(max_length = 100, null=True)

    
class TbMember(models.Model):
    fk_player = models.ForeignKey(TbPlayer,on_delete = models.CASCADE)
    fk_group = models.ForeignKey(TbGroup,on_delete = models.CASCADE) 
    cl_username =  models.CharField(max_length = 100, null=True)
    cl_password =  models.CharField(max_length = 100, null=True)


class TbMatchTeam(models.Model):
    cl_match_id = models.IntegerField(null=True)
    cl_team_id =  models.IntegerField(null=True)
    cl_aoe2_net_id = models.IntegerField(null=True)
    cl_civ = models.CharField(max_length = 100, null=True)
    cl_match_result = models.IntegerField(null=True)
    cl_created_at = models.DateTimeField(null = True)
    cl_update_at = models.DateTimeField(null = True)
    
class TbGameMatches(models.Model):
    cl_match_id = models.IntegerField(null=True)
    cl_started_at = models.DateTimeField(null = True)
    cl_finished_at = models.DateTimeField(null = True)
    cl_map = models.CharField(max_length = 100, null=True)
    cl_server = models.CharField(max_length = 100, null=True)
    cl_lobby_name = models.CharField(max_length = 100, null=True)
    cl_created_at = models.DateTimeField(null = True)
    cl_update_at = models.DateTimeField(null = True)
    
    