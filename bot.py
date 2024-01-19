from zhipuai import ZhipuAI

class Bot:
    def __init__(self, character, career, age, name):
        self.character = character
        self.career = career
        self.age = age
        self.name = name

    def response(self, content):
        client = ZhipuAI(api_key="")  # 填写您自己的APIKey
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=[
                {"role": "user", "content": "你是谁"},
                {"role": "assistant", "content": "我是人工智能助手"},
                {"role": "user", "content": "你叫什么名字"},
                {"role": "assistant", "content": "我叫chatGLM"},
                {"role": "user", "content": content}
            ],
        )
        return response.choices[0].message
