




from globalApp.models import TbPlayer


final_elo = 70



# To Do
to_do = """"
1. Fecth from TbMatches
2. Loops per Matches
3. Check latest match for win streak
4. Fetch data froma AOE API every 5 minutes
"""
def eloCalculationPerPLayer(
    alias,player_id,final_elo,status):
    
    data = TbPlayer.objects.get(cl_player_id = player_id)
    streak = 0
    if final_elo <= 50 :
        params_rating = 0.5
    elif 50 >= final_elo < 60:
        params_rating = 0.4
    elif 60 >= final_elo < 70:
        params_rating = 0.3
    
    if status == 'lose':
        final_elo +- params_rating
        streak = 0
        data.cl_last_lose_count = data.cl_last_lose_count + 1
    elif status == 'won':
        final_elo += params_rating
        streak += data.cl_win_streak
        data.cl_last_win_count = data.cl_last_win_count + 1
        
    data.cl_final_elo = data.cl_final_elo + params_rating
    data.cl_win_streak = streak
    data.cl_player_alias = alias
    
    data.save()



fetch_api = {
    
}
