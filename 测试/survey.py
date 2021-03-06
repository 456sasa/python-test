class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        results = self.responses
        print("Survey results")
        for result in results:
            print(f"- {result}")