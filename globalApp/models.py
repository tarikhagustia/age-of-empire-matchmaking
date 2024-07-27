from django.db import models

# Create your models here.
class TbPlayer(models.Model):
    cl_player_id = models.IntegerField(null=True)
    cl_player_name = models.CharField(max_length = 100, null=True)
    cl_avatar_url = models.CharField(max_length = 200, null=True)
    cl_player_alias = models.CharField(max_length = 100, null=True)
    cl_win_streak = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_last_win_count = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_last_lose_count = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    cl_final_elo = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    
class TbMember(models.Model):
    cl_username =  models.CharField(max_length = 100, null=True)
    cl_password =  models.CharField(max_length = 100, null=True)
    
class TbPlayerGameMatches(models.Model):
    cl_match_id = models.IntegerField(null=True)
    cl_player_id = models.IntegerField(null=True)
    cl_match_result = models.IntegerField(null=True)
    cl_started_at = models.DateTimeField(null = True)
    cl_finished_at = models.DateTimeField(null = True)
    cl_status = models.BooleanField(null=False)

class TbLog(models.Model):
    fk_member = models.ForeignKey(TbMember,on_delete = models.CASCADE)
    cl_log  = models.CharField(max_length = 100, null=True)
    