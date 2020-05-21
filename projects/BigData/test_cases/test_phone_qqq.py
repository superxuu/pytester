import time
import pytest


class TestPhoneQqq:
    apiName = 'phone_qqq'

    # 类级别的事务fixture被标记为autouse=true，这意味着类中的所有测试方法将使用这个fixture，而不需要在测试函数签名中声明它
    # @pytest.fixture(scope="module",params=["smtp.gmail.com", "mail.python.org"],autouse=True)
    @pytest.fixture(autouse=True)
    def handdler(self):
        print('pre do')
        self.msgid = 'xxxxxx' + time.strftime("%Y%m%d", time.localtime()) + str(int(time.time() * 100))
        time.sleep(1)
        yield
        print('post do')

    @pytest.mark.skip('跳过测试')
    def test_api(self,param):

        print(self.msgid)
        print(param)
