import pytest
from pathlib import Path

from openpyxl import load_workbook

from util.case_yaml_to_excel import get_yaml

# @pytest.fixture(scope='module')
# def get_data(request, load_testdata_from_caseexcel):
#     apiName = getattr(request.module, 'apiName')
#     # print(apiName)
#     return load_testdata_from_caseexcel('BigData', apiName)


from util.read_excel_data import load_testdata_from_caseexcel
from projects.BigData import pre_test

project = 'BigData'


def pytest_generate_tests(metafunc):
    global apiName
    apiName = []
    apiName.append(metafunc.cls.apiName)
    case_data_list = load_testdata_from_caseexcel(project, apiName[0])
    metafunc.parametrize('param', handdle_data(case_data_list))


def handdle_data(data):
    __import__(f'projects.BigData.pre_test.{apiName[0]}')
    func = getattr(pre_test, apiName[0])

    # 对该项目下所有接口的所有入参做同样的事情
    print('对该项目下所有接口的所有入参做同样的事情')

    return func.handdle_data(data)

# from projects.BigData.pre_test import phone_qqq
# from projects.BigData.pre_test import phone_check
