from globalApp.models import TbPlayer
from django.http import JsonResponse
from django.core import serializers

def addEditPlayer(request):
    data = request.POST
    try:
        if data['player_id']:
            player = TbPlayer.objects.get(id=data['player_id'])
    except:
        player = TbPlayer()
        
    player.cl_avatar_url = data['avatar_url']
    player.cl_player_name = data['player_name']
    
    player.save()
    
    return JsonResponse(
        data={
            'result' : 'success'
        }
    )
    
def getAllPlayer(request):
    all_players = TbPlayer.objects.all()
    data = serializers.serialize('json', all_players)
    return JsonResponse(data, safe=False)    
    
        
    