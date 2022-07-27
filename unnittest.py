import unittest
# from src import catly_translate
from src.catly_translate import utils


# translate = catly_translate.translate
translate = utils.translate
class Test(unittest.TestCase):
    def test_common_case_0(self):
        self.assertEqual(translate("hello"), ["你好"])
        
    def test_common_case_1(self):
        self.assertEqual(translate("こんにちは"), ["你好"])
    
    def test_common_case_2(self):
        self.assertEqual(translate("Hello\nWorld"), ['你好', '世界'])
    
    def test_common_case_3(self):
        self.assertEqual(translate("こんにちは\r\n世界"), ['你好', '世界'])
    

if __name__ == "__main__":
    debug = 0
    if debug:
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(Test))
        unittest.TextTestRunner().run(suite)

    # print(translate("#Hello"))
    print(translate("hello"))
    print(translate("hello"))
    print(translate("#hello"))
    print(translate("こんにちは"))
    # print(translate(["hello"]))
    # print(catly_translate.translate("我的门卡掉了", to_lang="en"))
    # print(catly_translate.translate('Hello', "en", "jp"))