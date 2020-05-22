
from util.read_excel_data import load_testdata_from_caseexcel
from projects.VBA import pre_test

project = 'VBA'


def pytest_generate_tests(metafunc):
    global apiName
    apiName = []
    apiName.append(metafunc.cls.apiName)
    case_data_list = load_testdata_from_caseexcel(project, apiName[0])
    metafunc.parametrize('param', handdle_data(case_data_list))


def handdle_data(data):
    __import__(f'projects.VBA.pre_test.{apiName[0]}')
    func = getattr(pre_test, apiName[0])

    # 对该项目下所有接口的所有入参做同样的事情
    print(f'对{project}项目下所有接口的所有入参做同样的事情')


    return func.handdle_data(data)
