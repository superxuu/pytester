import time
from parameterized import parameterized, parameterized_class
import pytest
from ..pre_test.pre_phone_test import *

# from projects.BigData.conftest import get_data

# 接口名称、sheet名称
apiName = 'phone_test'

# a = [{'CaseName': '测试案例1', 'key1': 1, 'key3': 'aaa', 'key5': '萨达', 'key2': '沃尔沃群所', 'key4': 'qqq111', 'srcCode': '0000', 'srcMsg': 'srcMsg111'}, {'CaseName': '测试案例2', 'key1': 2, 'key3': 'bbb', 'key5': '沙发上', 'key2': None, 'key4': 'www222', 'srcCode': '0001', 'srcMsg': 'srcMsg112'}, {'CaseName': '测试案例3', 'key1': 3, 'key3': 'ccc', 'key5': None, 'key2': '萨达', 'key4': 'eee333', 'srcCode': '0002', 'srcMsg': 'srcMsg113'}, {'CaseName': '测试案例4', 'key1': 4, 'key3': 'ddd', 'key5': '是否', 'key2': None, 'key4': 'rrr444', 'srcCode': '0003', 'srcMsg': 'srcMsg114'}, {'CaseName': '测试案例5', 'key1': 5, 'key3': 'eee', 'key5': '水电费', 'key2': 1231234, 'key4': 'ttt555', 'srcCode': '0004', 'srcMsg': 'srcMsg115'}, {'CaseName': '测试案例6', 'key1': 6, 'key3': 'fff', 'key5': None, 'key2': None, 'key4': None, 'srcCode': '0005', 'srcMsg': 'srcMsg116'}]
a = [1, 2]





class TestPhoneCheck:
    @pytest.fixture(scope='module', autouse=True)
    def ddt_data(get_data):
        print('ddt_data')
        data = get_data
        request_info = data.pop(-1)
        print(request_info)
        # __import__(f'BigData.pre_test.pre_phone_test.pre_phone_test',fromlist=True)
        return pre_phone_test.handdle_data(data)

    @pytest.fixture(autouse=True)
    def handdler(self):
        print('pre do')
        self.msgid = 'xxxxxx' + time.strftime("%Y%m%d", time.localtime()) + str(int(time.time() * 100))
        yield
        print('post do')



    # 类级别的事务fixture被标记为autouse=true，这意味着类中的所有测试方法将使用这个fixture，而不需要在测试函数签名中声明它
    # @pytest.fixture(scope="module",params=["smtp.gmail.com", "mail.python.org"],autouse=True)


    # @pytest.mark.skip(reason="no way of currently testing this")a
    # @pytest.mark.skipif(3<2, reason="3>2")
    @pytest.mark.parametrize('param', pre_phone_test.www)
    # @pytest.mark.parametrize('param', a)
    # @pytest.mark.usefixtures('ddt_data')
    def test_ddt(self, param):
        print(self.msgid)
        # print(ddt_data)
        print('param::::=', param)
        # print(pre_phone_test.www)
        # print(params)
        # data_list  = load_testdata_from_caseexcel
        # print(data_list)

        # if data_list[-1]['apiName'] != apiName:
        #     print('apiName不匹配！')
        # else:
        #     print(data_list)
        #     assert 1==1
        #     print(445566)

    # def test_1(self):
    #     print('test_1')
    #
    # def test_2(self):
    #     print('test_2')
