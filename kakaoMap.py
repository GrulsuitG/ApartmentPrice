import pprint
import pandas as pd
import requests

import json

# CONSTANT
NAME = 0
CODE = 1
DISTANCE = 2

# 1
# 지하철 - 50m 50 / 300m 30 / 500m 20 
# 학교 20

# 2
# 마트 10

# 3
# 카페 1 
# 은행 1
# 병원 1

condition = [['station1', 'SW8', 50],
             ['station2', 'SW8', 300],
             ['station3', 'SW8', 500],
             ['market', 'MT1', 1000],
             ['school', 'SC4', 500],
             ['bank', 'BK9', 500],
             ['cafe', 'CE7', 500],
             ['hospital', 'HP8', 500]]


headers = {"Authorization": "KakaoAK c652e194fdb5eda29c468c1cb18cc18a"}


def getNumberOfAroundService():
    url = 'https://dapi.kakao.com/v2/local/search/category.json'
    res = pd.DataFrame()
    data = pd.read_csv('point.csv',index_col=False, dtype={'adress': str, 'Latitude':str, 'Longitude':str})
    for d in data.iloc:
        info = {'address' : d['address']}
        for i in range(0, len(condition)):
            
            params = {'x' : d['Longitude'], 'y' : d['Latitude'], 'radius' : condition[i][DISTANCE], 'category_group_code' : condition[i][CODE]}
            if(i>2):
                total = requests.get(url, params=params, headers=headers).json()['meta']['total_count']
                if(condition[i][NAME] == 'market'):
                    total = int(total)*10
                elif(condition[i][NAME] == 'school'):
                    total = int(total)*20
                info.update({condition[i][NAME] : total})
            else : 
                if(condition[i][NAME] == 'station1'):
                    total = int(requests.get(url, params=params, headers=headers).json()['meta']['total_count'])*50
                elif(condition[i][NAME] == 'station2'):
                    total += int(requests.get(url, params=params, headers=headers).json()['meta']['total_count'])*30
                elif(condition[i][NAME] == 'station3'):
                    total += int(requests.get(url, params=params, headers=headers).json()['meta']['total_count'])*20
                
                    info.update({'station' : total})
        pprint.pprint(info)       
        res = res.append(info, ignore_index=True)
    return res

def getPoint():
    url = 'https://dapi.kakao.com/v2/local/search/address.json'
    res = pd.DataFrame()
    data = pd.read_csv('address_t.csv', dtype={'address':str})
    
    for d in data.iloc:
        # info = {'address' : d['address']}
        params = {"query" : d['address']}
        Point = requests.get(url, params=params,headers=headers).json()['documents'][0]
        pprint.pprint({'address' : d, 'Longitude': Point['x'], 'Latitude': Point['y']})

        res = res.append({'address' : d['address'], 'Longitude': Point['x'], 'Latitude': Point['y']}, ignore_index=True)
    return res

    
# res = getPoint()
# res.to_csv('point_t.csv', encoding='utf-8-sig')

res = getNumberOfAroundService()
res.to_csv('result.csv', encoding='utf-8-sig')
