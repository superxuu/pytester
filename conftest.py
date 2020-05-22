import pytest
from pathlib import Path
from pprint import pprint
from openpyxl import load_workbook

from util.read_excel_data import get_yaml


# @pytest.fixture(scope='session')
# def load_testdata_from_caseexcel():
#     def _load_testdata_from_caseexcel(project, apiName):
#         excel_path = Path(f'projects/{project}/data/{project}.xlsx')
#         wb = load_workbook(excel_path)
#         # ws = wb.get_sheet_by_name('phone_test')#弃用
#         ws = wb[apiName]
#         title = list(ws.values)[1]
#         test_data = list(ws.values)[2:]
#         exec_index = title.index('exec')
#         case_data_list = []
#         for i in test_data:
#             if i[exec_index] in ['Y','y']:
#                 case_data_dict = dict(zip(title,i[:-2]))
#                 case_data_list.append(case_data_dict)
#         yaml_file = Path(f'projects/{project}/conf/{apiName}.yaml')
#         api_info = get_yaml(yaml_file)
#         api_info.pop('parmas')
#         api_info.pop('response_assert')
#         case_data_list.append(api_info)
#         return case_data_list
#     return _load_testdata_from_caseexcel

# def pytest_generate_tests(metafunc):
#     def _load_testdata_from_caseexcel(project, apiName):
#         excel_path = Path(f'projects/{project}/data/{project}.xlsx')
#         wb = load_workbook(excel_path)
#         # ws = wb.get_sheet_by_name('phone_test')#弃用
#         ws = wb[apiName]
#         title = list(ws.values)[1]
#         test_data = list(ws.values)[2:]
#         exec_index = title.index('exec')
#         case_data_list = []
#         for i in test_data:
#             if i[exec_index] in ['Y','y']:
#                 case_data_dict = dict(zip(title,i[:-2]))
#                 case_data_list.append(case_data_dict)
#         yaml_file = Path(f'projects/{project}/conf/{apiName}.yaml')
#         api_info = get_yaml(yaml_file)
#         api_info.pop('parmas')
#         api_info.pop('response_assert')
#         case_data_list.append(api_info)
#         metafunc.parametrize('parmas', case_data_list)
#     return _load_testdata_from_caseexcel

# def load_testdata_from_caseexcel(project, apiName):
#     excel_path = Path(f'projects/{project}/data/{project}.xlsx')
#     wb = load_workbook(excel_path)
#     # ws = wb.get_sheet_by_name('phone_test')#弃用
#     ws = wb[apiName]
#     title = list(ws.values)[1]
#     test_data = list(ws.values)[2:]
#     exec_index = title.index('exec')
#     case_data_list = []
#     for i in test_data:
#         if i[exec_index] in ['Y','y']:
#             case_data_dict = dict(zip(title,i[:-2]))
#             case_data_list.append(case_data_dict)
#     yaml_file = Path(f'projects/{project}/conf/{apiName}.yaml')
#     api_info = get_yaml(yaml_file)
#     api_info.pop('parmas')
#     api_info.pop('response_assert')
#     # case_data_list.append(api_info)
#     # metafunc.parametrize('parmas', case_data_list)
#     return api_info, case_data_list

if __name__ == '__main__':
    # load_testdata_from_caseexcel('BigData')
    pass
