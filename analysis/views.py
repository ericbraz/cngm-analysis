import os
import json
from django.http import JsonResponse
from analysis.data_importer.constants import INNER_SUBFOLDER

def cngm(request):
    if request.method == 'GET':
        json_file_path = os.path.join(INNER_SUBFOLDER, 'cngm.json')
        print(json_file_path)

        if os.path.exists(json_file_path):
            # Read the JSON file
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                print(data)

            return JsonResponse(data)
        else:
            return JsonResponse({'message': 'The JSON file does not exist.'})

    else:
        response = {
            'message': 'Wrong method',
        }
        return JsonResponse(response)
