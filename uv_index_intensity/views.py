from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uv_index_intensity.models import Data

# Create your views here.
@csrf_exempt
def index(request):
    uvIntensity = Data.objects.last()
    uvIndex = Data.objects.last()

    if (uvIntensity is None):
        uvIntensity = "No data"
    else:
        uvIntensity = uvIntensity.uvIntensity
    
    if (uvIndex is None):
        uvIndex = -1
    else:
        uvIndex = uvIndex.uvIndex

    context = {'uvIntensity': uvIntensity, 'uvIndex': int(uvIndex)}

    return render(request, 'index.html', context)

@csrf_exempt
def recordData(request):
    data = Data(
        uvIntensity = request.POST['uvIntensity'],
        uvIndex = request.POST['uvIndex']
    )

    data.save()

    return JsonResponse({'message': 'Data was saved succesfully'})