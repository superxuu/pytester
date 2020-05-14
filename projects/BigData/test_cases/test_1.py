import allure
import pytest


class Testpytest():

    def test_with_no_severity_label(self):
        assert 1==1

    def test_with_trivial_severity(self):
        assert 1 == 12

    def test_with_normal_severity(self):
        assert 1 == 1
