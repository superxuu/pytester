import shutil
from pathlib import Path


def create_project(project_name):
    p = Path('../projects')
    # 获取已存在的所有项目名称列表
    projects_list = [pj.name for pj in p.glob('*') if pj.is_dir() and pj.name != '__pycache__']
    print('当前已存在的所有项目：', projects_list)
    if project_name in projects_list:
        print(f'{project_name}项目已存在，放弃创建')
    else:
        print('开始创建新的项目目录')
        project_path = p / project_name
        print(project_path)
        p_conf = project_path / 'conf'
        p_data = project_path / 'data'
        p_pre_test = project_path / 'pre_test'
        p_script = project_path / 'script'
        p_test_cases = project_path / 'test_cases'
        p_conftest = project_path / 'conftest.py'

        p_pre_test_init = p_pre_test / '__init__.py'
        p_script_init = p_script / '__init__.py'
        p_test_cases_init = p_test_cases / '__init__.py'
        p_test_cases_conftest = p_test_cases / 'conftest.py'

        Path.mkdir(project_path, parents=False, exist_ok=False)
        Path.mkdir(p_conf, parents=False, exist_ok=False)
        Path.mkdir(p_data, parents=False, exist_ok=False)
        Path.mkdir(p_pre_test, parents=False, exist_ok=False)
        Path.mkdir(p_script, parents=False, exist_ok=False)
        Path.mkdir(p_test_cases, parents=False, exist_ok=False)
        Path.touch(p_conftest, exist_ok=False)
        Path.touch(p_pre_test_init, exist_ok=False)
        Path.touch(p_script_init, exist_ok=False)
        Path.touch(p_test_cases_init, exist_ok=False)
        Path.touch(p_test_cases_conftest, exist_ok=False)
        casedata_excel = Path('../lib/casedata.xlsx')
        exampleApi_yaml = Path('../lib/exampleApi.yaml')
        phone_check_yaml = Path('../lib/phone_check.yaml')

        # 将示例yaml与案例excel复制到对应目录
        shutil.copyfile(casedata_excel, p_data / f'{project_name}.xlsx')
        shutil.copyfile(exampleApi_yaml, p_conf / 'exampleApi.yaml')
        shutil.copyfile(phone_check_yaml, p_conf / 'phone_check.yaml')
        # 写入项目级conftest.py的内容
        with open(p_conftest, mode='w', encoding='UTF-8') as f:
            content = f'''
from util.read_excel_data import load_testdata_from_caseexcel
from projects.{project_name} import pre_test

project = '{project_name}'


def pytest_generate_tests(metafunc):
    global apiName
    apiName = []
    apiName.append(metafunc.cls.apiName)
    case_data_list = load_testdata_from_caseexcel(project, apiName[0])
    metafunc.parametrize('param', handdle_data(case_data_list))


def handdle_data(data):
    __import__(f'projects.{project_name}.pre_test.{{apiName[0]}}')
    func = getattr(pre_test, apiName[0])

    # 对该项目下所有接口的所有入参做同样的事情
    print(f'对{{project}}项目下所有接口的所有入参做同样的事情')


    return func.handdle_data(data)
'''
            f.write(content)

        print(f'{project_name}项目目录创建完毕')


if __name__ == '__main__':
    create_project('VBA')
