import time
from parameterized import parameterized, parameterized_class
import pytest


class TestPhoneCheck:
    apiName = 'phone_check'
    # request_info =[]
    # params =[]
    # @pytest.fixture(scope='module', autouse=True)#scope='module',
    # def ddt_data(self, get_data):
    #     global request_info,params_data
    #     print('ddt_data')
    #     data = get_data
    #     request_info = data.pop(-1)
    #     params = pre_phone_test.handdle_data(data)



    # 类级别的事务fixture被标记为autouse=true，这意味着类中的所有测试方法将使用这个fixture，而不需要在测试函数签名中声明它
    # @pytest.fixture(scope="module",params=["smtp.gmail.com", "mail.python.org"],autouse=True)
    @pytest.fixture(autouse=True)
    def handdler(self):
        print('pre do')
        self.msgid = 'xxxxxx' + time.strftime("%Y%m%d", time.localtime()) + str(int(time.time() * 100))
        time.sleep(1)
        yield
        print('post do')

    # @pytest.mark.skip(reason="no way of currently testing this")a
    # @pytest.mark.skipif(3<2, reason="3>2")
    # @pytest.mark.parametrize('param', pre_phone_test.www)
    # @pytest.mark.parametrize('param', params)
    # @pytest.mark.usefixtures('ddt_data')
    def test_ddt(self,param):
        # print('params_data:',params_data)
        # print('request_info:',request_info)

        print(self.msgid)
        print(param)
        # print('param::::=', param)

        # if data_list[-1]['apiName'] != apiName:
        #     print('apiName不匹配！')
        # else:
        #     print(data_list)
        #     assert 1==1
        #     print(445566)

    # def test_1(self,param):
    #     print('test_1')
    #
    # def test_2(self,param):
    #     print('test_2')
