import pytest
import os
import subprocess











if __name__ == '__main__':
    case_dir = 'projects/'
    # args = ['-s', '-v', f'{case_dir}', '--alluredir=report/allure-results', '--clean-alluredir']
    args = ['-s', '-v', f'{case_dir}']
    pytest.main(args)
    # os.system('allure generate report/allure-results --clean -o report/allure-report')
    # subprocess.Popen(['D:\\Program Files\\allure-2.13.1\\bin\\allure.bat', 'generate', 'report/allure-results', '--clean', '-o', 'report/allure-report'],
    #                  shell=True).wait()
