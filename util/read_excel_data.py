from pathlib import Path

from openpyxl import load_workbook

from util.case_yaml_to_excel import get_yaml


def load_testdata_from_caseexcel(project, apiName):
    """
    生成的单个案例格式如下：
    {'CaseName': '测试案例1', 'request_params': {'key1': 1, 'key2': '沃尔沃群所', 'key3': 'aaa', 'key4': 'qqq111', 'key5': '萨达'}, 'response_assert': {'srcCode': '0000', 'srcMsg': 'srcMsg111'}, 'request_info': {'apiName': 'phone_check', 'request_url': 'http://127.0.0.1/edh/api?uid=sd0001&api=N001_QY00100_V001&querymode=0&msgid=', 'request_method': 'post', 'headers': {'token': None}}}
    最终返回的是由单个案例组成的list：    [{},{},{}]

    :param project: 项目名，例如BigData
    :param apiName: 项目下具体接口名
    :return:
    """

    yaml_file = Path(f'projects/{project}/conf/{apiName}.yaml')
    request_info = get_yaml(yaml_file)
    parmas_list = request_info.pop('parmas')
    response_assert_list = request_info.pop('response_assert')

    excel_path = Path(f'projects/{project}/data/{project}.xlsx')
    wb = load_workbook(excel_path)
    # ws = wb.get_sheet_by_name('phone_test')#弃用
    ws = wb[apiName]
    title = list(ws.values)[1]
    test_data = list(ws.values)[2:]
    wb.close()
    exec_index = title.index('exec')
    case_data_list = []
    for i in test_data:
        if i[exec_index] in ['Y', 'y']:
            case_data_dict = {}
            request_params_dict = {}
            response_assert_dict = {}
            data_dict = dict(zip(title, i[:-2]))
            for param in parmas_list:
                request_params_dict[param] = data_dict[param]
            for assert_key in response_assert_list:
                response_assert_dict[assert_key] = data_dict[assert_key]
            case_data_dict['CaseName'] = data_dict['CaseName']
            case_data_dict['request_params'] = request_params_dict
            case_data_dict['response_assert'] = response_assert_dict
            case_data_dict['request_info'] = request_info
            case_data_list.append(case_data_dict)
    return case_data_list
