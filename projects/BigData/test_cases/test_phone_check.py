import time
from parameterized import parameterized, parameterized_class
import pytest
import requests


class TestPhoneCheck:
    apiName = 'phone_check'

    # scope='module'意味着该fixture只在案例开始前运行一次
    @pytest.fixture(scope='module', autouse=True)
    def ddt_data(self):
        pass

    # 类级别的事务fixture被标记为autouse=true，这意味着类中的所有测试方法将使用这个fixture，而不需要在测试函数签名中声明它
    @pytest.fixture(autouse=True)
    def handdler(self):
        print('pre do')
        self.msgid = 'xxxxxx' + time.strftime("%Y%m%d", time.localtime()) + str(int(time.time() * 100))
        time.sleep(1)
        yield
        print('post do')

    # @pytest.mark.skip(reason="no way of currently testing this")a
    # @pytest.mark.skipif(3<2, reason="3>2")
    def test_ddt(self, param):
        print(self.msgid)
        print(param)
        if param['request_info']['apiName'] != TestPhoneCheck.apiName:
            print('apiName不匹配！')
        else:
            url = param['request_info']['request_url']
            header = param['request_info']['headers']
            data = param['request_params']
            responce_assert = param['response_assert']

            res = requests.post(url, data=data, headers=header).json

            assert responce_assert['srcCode'] == res['srcCode']
            assert responce_assert['srcMsg'] == res['srcMsg']
