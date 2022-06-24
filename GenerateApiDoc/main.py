import json
from docxtpl import DocxTemplate
import jinja2
import traceback
import pdb

paramTypeDic = {
    '0': 'String',
    '1': 'File',
    '2': 'Json',
    '3': 'Int',
    '4': 'Float',
    '5': 'Double',
    '6': 'Date',
    '7': 'Datetime',
    '8': 'Boolean',
    '9': 'Byte',
    '10': 'Short',
    '11': 'Long',
    '12': 'Array',
    '13': 'Object',
    '14': 'Number',
    '15': 'Null',
    'char': 'Char'
}

apiRequestTypeDic = {
    '0': 'POST',
    '1': 'GET',
    '2': 'PUT',
    '3': 'DEL',
    '4': 'HEAD',
    '5': 'OPTIONS',
    '6': 'PATCH'
}


def get_dict_data(d, name):
    if not d:
        return ''
    if name not in d:
        return ''
    return d[name]


def get_request_type(api_data):
    tmp = str(get_dict_data(get_dict_data(api_data, 'baseInfo'), 'apiRequestType'))
    if tmp in apiRequestTypeDic:
        return apiRequestTypeDic[tmp]
    return None


def get_param_type(param):
    tmp = get_dict_data(param, 'paramType')
    if tmp in paramTypeDic:
        return paramTypeDic[tmp]
    return None


def type_format(value):
    if isinstance(value, int) or isinstance(value, float):
        return paramTypeDic['14']
    if isinstance(value, list):
        return paramTypeDic['12']
    if isinstance(value, str):
        return paramTypeDic['0']
    if isinstance(value, bool):
        return paramTypeDic['8']
    if isinstance(value, dict):
        return paramTypeDic['13']
    return ''


def get_result_params(payload):
    result_params = []
    if not payload:
        return result_params
    if payload == 'null':
        return result_params
    if isinstance(payload, list) and len(payload) and isinstance(payload[0], dict):
        for kname in payload[0]:
            r_data = {
                'paramKey': kname,
                'paramName': payload[0][kname],
                'paramType': type_format(payload[0][kname])
            }
            if isinstance(payload[0][kname], list) or isinstance(payload[0][kname], dict):
                r_data['paramName'] = ''
                r_data['childs'] = get_result_params(payload[0][kname])
            result_params.append(r_data)

    if isinstance(payload, dict) and len(payload):
        for kname in payload:
            r_data = {
                'paramKey': kname,
                'paramName': payload[kname],
                'paramType': type_format(payload[kname])
            }
            if isinstance(payload[kname], list) or isinstance(payload[kname], dict):
                r_data['paramName'] = ''
                r_data['childs'] = get_result_params(payload[kname])
            result_params.append(r_data)

    return result_params


def get_api_data(api):
    apiData = {
        'apiName': get_dict_data(get_dict_data(api, 'baseInfo'), 'apiName'),
        'apiURI': get_dict_data(get_dict_data(api, 'baseInfo'), 'apiURI'),
        'apiRequestType': get_request_type(api),
        'result': get_dict_data(get_dict_data(api, 'baseInfo'), 'apiSuccessMock')
    }
    if not apiData['result']:
        resultInfo = get_dict_data(api, 'resultInfo')
        if resultInfo:
            apiData['result'] = resultInfo[0]['raw']
    requestParams = []
    resultParams = []

    for p in get_dict_data(api, 'restfulParam'):
        p_data = {
            'paramKey': get_dict_data(p, 'paramKey'),
            'paramName': get_dict_data(p, 'paramName') + ' ' + get_dict_data(p, 'paramValue'),
            'paramType': get_param_type(p),
            'paramNotNull': get_dict_data(p, 'paramNotNull')
        }
        requestParams.append(p_data)

    for p in get_dict_data(api, 'urlParam'):
        p_data = {
            'paramKey': get_dict_data(p, 'paramKey'),
            'paramName': get_dict_data(p, 'paramName') + ' ' + get_dict_data(p, 'paramValue'),
            'paramType': get_param_type(p),
            'paramNotNull': get_dict_data(p, 'paramNotNull')
        }
        requestParams.append(p_data)
    for p in get_dict_data(api, 'requestInfo'):
        p_data = {
            'paramKey': get_dict_data(p, 'paramKey'),
            'paramName': get_dict_data(p, 'paramName') + ' ' + get_dict_data(p, 'paramValue'),
            'paramType': get_param_type(p),
            'paramNotNull': get_dict_data(p, 'paramNotNull')
        }
        requestParams.append(p_data)

    reqBody = get_dict_data(get_dict_data(api, 'baseInfo'), 'apiRequestRaw')
    if reqBody and isinstance(reqBody, str):
        # 中文是否乱码？
        bodyDict = json.loads(reqBody)
        for p_key in bodyDict:
            p_data = {
                'paramKey': p_key,
                'paramName': bodyDict[p_key],
                'paramType': type_format(bodyDict[p_key]),
                'paramNotNull': '0'
            }
            requestParams.append(p_data)
    result = json.loads(apiData['result'].replace('\r\n', ''))

    resultParams = get_result_params(result['payload'])
    apiData['requestParams'] = requestParams
    apiData['resultParams'] = resultParams
    return apiData


def get_group_data(group):
    data = {
        'groupName': group['groupName'],
        'apiList': [],
        'childGroupList': []
    }
    apiList = group.get('apiList')
    if apiList:
        for api in apiList:
            try:
                apiData = get_api_data(api)
                data['apiList'].append(apiData)
            except Exception as e:
                print(get_dict_data(api, 'groupName') + '-' + get_dict_data(get_dict_data(api, 'baseInfo'),
                                                                            'apiName') + '失败')
                print(e)
                traceback.print_exc()
                # pdb.set_trace()

    childGroupList = group.get('childGroupList')
    if childGroupList:
        for childGroup in childGroupList:
            try:
                data['childGroupList'].append(get_group_data(childGroup))
            except Exception:
                print(childGroup['groupName'] + '失败')

    return data


filename = '4'

with open(f'./{filename}.json', 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    data = get_group_data(load_dict)
    # print(data)
    # groupName 分组名
    # apiList 接口列表
    #     接口字典：
    #       baseInfo.apiName 接口名
    #       baseInfo.apiURI 接口地址
    #       baseInfo.apiRequestType 请求类型1-get 0-post 2-put 3-del
    #       baseInfo.'apiRequestRaw'  body请求参数，从里面解析字段，类型为string才认为有内容
    #       'restfulParam' 列表  rest参数列表：'paramKey' 字段名  'paramName' 说明  'paramType'类型 （字段不一定有）
    #       urlParam列表   Query参数列表: 'paramKey' 字段名  'paramName' 说明  'paramType'类型
    #  baseInfo.'apiSuccessMock' 返回示例

    # a = data['childGroupList'][0]['apiList'][0]
    tpl = DocxTemplate('./tpl3.docx')
    tpl.render(data)
    tpl.save(f'./rs{filename}.docx')

# rest参数、Query参数、body里的参数，都写到参数列表
# 从返回成功示例里解析返回字段
# 字段表格不要示例一栏，示例写在说明里
