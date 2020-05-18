from pathlib import Path

from openpyxl import load_workbook

from util.case_yaml_to_excel import get_yaml


def load_testdata_from_caseexcel(project, apiName):
    yaml_file = Path(f'projects/{project}/conf/{apiName}.yaml')
    api_info = get_yaml(yaml_file)
    api_info.pop('parmas')
    api_info.pop('response_assert')

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
        if i[exec_index] in ['Y','y']:
            case_data_dict = dict(zip(title,i[:-2]))
            case_data_dict.update(api_info)
            case_data_list.append(case_data_dict)

    return case_data_list