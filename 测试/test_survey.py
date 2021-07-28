import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "what language did you first learn to speak"
        self.my_survey = AnonymousSurvey(question)
        self.languages=['English','Chinese','French']
    
    """测试单个答案会被妥善存储"""
    def test_store_response(self):
        self.my_survey.store_response('English')
        self.assertIn('English',self.my_survey.responses)

    def test_store_three_response(self):
        for language in  self.languages:
            self.my_survey.store_response(language)

        for result in self.my_survey.responses:
            self.assertIn(result,self.my_survey.responses)
       

if __name__ =="__main__":
    unittest.main()