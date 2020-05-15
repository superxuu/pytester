import pytest


@pytest.fixture(scope='module')
def get_data(request, load_testdata_from_caseexcel):
    apiName =  getattr(request.module,'apiName')
    # print(apiName)
    return load_testdata_from_caseexcel('BigData',apiName)

#
# @pytest.fixture(params=data)
# def ddt_data(request):
#     print(request.param)
#     yield request.param




# class Handdler(object):
#     @staticmethod
#     def handdle_data(data):
#
#         return data


