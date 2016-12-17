#!/usr/bin/env python
import argparse
import json
import sys

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#def main(input_file, output_filename):
def main():
    request_list = []
    content_json_obj = {
        'content': sys.argv[1]
    }
    feature_json_obj = []
    feature_json_obj.append({
                'maxResults': 1,
                'type': 'FACE_DETECTION',
            })
    request_list.append({
            'features': feature_json_obj,
            'image': content_json_obj,
    })
    json_request = json.dumps({'requests': request_list})
    return json_request


if __name__ == '__main__':
    data = main()
    api_key = # PASTE GOOGLE CLOUD VISION API KEY HERE
    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key='+api_key,
    data=data, verify = False,
    headers={'Content-Type': 'application/json'})
    res = json.loads(response.text)
    if len(res['responses'][0]) == 0:
        print('same')
    else:
        joy = res['responses'][0]['faceAnnotations'][0]['joyLikelihood']
        sorrow = res['responses'][0]['faceAnnotations'][0]['sorrowLikelihood']
        anger = res['responses'][0]['faceAnnotations'][0]['angerLikelihood']
        surprise = res['responses'][0]['faceAnnotations'][0]['surpriseLikelihood']
        # print('joy: ' + joy)
        # print('sorrow: ' + sorrow)
        # print('anger: ' + anger)
        # print('surprise: ' + surprise)
        # print('\n')
        if joy == 'VERY_LIKELY':
            print('joy')
        elif sorrow == 'VERY_LIKELY':
            print('sorrow')
        elif anger == 'VERY_LIKELY':
            print('anger')
        elif surprise == 'VERY_LIKELY':
            print('surprise')
        elif joy == 'LIKELY':
            print('joy')
        elif sorrow == 'LIKELY':
            print('sorrow')
        elif anger == 'LIKELY':
            print('anger')
        elif surprise == 'LIKELY':
            print('surprise')
#        elif joy == 'UNLIKELY':
#            print('joy')
#        elif sorrow == 'UNLIKELY':
#            print('sorrow')
#        elif anger == 'UNLIKELY':
#            print('anger')
#        elif surprise == 'UNLIKELY':
#            print('surprise')
        else:
            print('same')
