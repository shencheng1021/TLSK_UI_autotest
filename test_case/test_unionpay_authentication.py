# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 银联商户合作资料认证资料收集测试
@time: 2022/4/13 9:34
"""
import json
import time

import allure
import pytest

from base1.base_util import BaseUtil
from common import dir_util
from common.request_util import RequestUtil
from common.yaml_util import YamlUtil
from page_base.union_identify_page import UnionIdentifyPage

@allure.feature('银联认证商户合作资料填报UI自动化测试')
class TestUnionpayAuth(BaseUtil):

    @allure.title('获取商户合作资料填报页面url')
    @pytest.mark.parametrize('caseinfo',YamlUtil().read_yaml(dir_util.testcase_dir,'union_geturl.yml'))
    def test_get_authurl(self,caseinfo):
        method=caseinfo['request']['method']
        url=caseinfo['request']['url']
        headers=caseinfo['request']['headers']
        caseinfo['request']['data']['companyName'] = YamlUtil().read_extract_yaml('companyName')
        caseinfo['request']['data']['busiLiceNo'] = YamlUtil().read_extract_yaml('busiLiceNo')
        data=json.dumps(caseinfo['request']['data'])
        rep=RequestUtil().send_request(method,url,headers=headers,data=data)
        result=json.loads(rep)
        YamlUtil().write_extract_yaml({'identifyPage': result['identifyPage']})
        UIP=UnionIdentifyPage(self.driver)
        UIP.assertEqual(caseinfo['assert'],result['status'])

    @allure.title('进入商户合作资料填报页面')
    def test_goto_identifypage(self):
        UIP = UnionIdentifyPage(self.driver)
        url=YamlUtil().read_extract_yaml('identifyPage')
        UIP.goto_identify_page(url)
        actual=UIP.check_data_description_alert()
        UIP.assertEqual('上传资料说明',actual)

    @allure.title('完善商户合作资料信息，并提交')
    def test_redact_information(self):
        url = YamlUtil().read_extract_yaml('identifyPage')
        business_name=YamlUtil().read_extract_yaml('companyName')
        UIP = UnionIdentifyPage(self.driver)
        UIP.goto_identify_page(url)
        UIP.input_business_information('营业执照.jpg',business_name)
        UIP.input_legal_information('身份证正面.jpg','身份证背面.jpg','17745474453')
        UIP.input_contact_person_information('身份证正面.jpg','身份证背面.jpg','17745474454')
        UIP.click_next_step_button()
        UIP.input_acc_ifm('账户信息.jpg','4575457545454',business_name,'中国建设银行股份有限公司成都天府新城支行','成都天府新区')
        UIP.click_acc_next_step()
        UIP.upload_scene_proof('场景说明.pdf')
        UIP.upload_office_space(['办公场所01.jpg','办公场所02.jpg'])
        UIP.upload_product_picture(['商品图片01.jpg','商品图片02.jpg'])
        UIP.upload_door(['门头招牌01.jpg'])
        UIP.upload_auth_confirm('成员资金管理授权确认书.pdf')
        UIP.upload_business_certificate(['经营证明01.jpg'])
        UIP.upload_agreement('平台入驻协议.pdf')
        UIP.upload_merchants_auth('特约商户授权书.pdf')
        UIP.upload_merchants_front('身份证正面.jpg')
        UIP.upload_merchants_back('身份证背面.jpg')
        UIP.upload_other(['其他文件01.pdf','其他文件02.pdf'])
        UIP.click_submit()
        actual=UIP.check_submit_success()
        UIP.assertEqual('银联进件资料已提交审核，审核进度等待平台通知！',actual)


if __name__ == '__main__':
    pytest.main()

