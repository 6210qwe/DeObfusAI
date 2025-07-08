from openai import OpenAI

class DeepSeekChat:
    # def __init__(self, api_key="sk-3eff2abfca0a4f36a46a3b1a47892668", base_url="https://api.deepseek.com"):
    def __init__(self, api_key="sk-bc6d895f807447f1b706c41f1ce1f4d4", base_url="https://api.deepseek.com"):
        """
        初始化 DeepSeekChat 客户端
        :param api_key: DeepSeek API 密钥
        :param base_url: DeepSeek API 基础 URL
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def get_chat_response(self, system_message, user_message, model="deepseek-chat", stream=False):
        """
        获取聊天响应
        :param system_message: 系统消息内容
        :param user_message: 用户消息内容
        :param model: 使用的模型名称，默认为 "deepseek-chat"
        :param stream: 是否使用流式响应，默认为 False
        :return: 模型生成的响应内容
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
            stream=stream
        )
        return response.choices[0].message.content


# 使用示例
if __name__ == "__main__":
    # 初始化 DeepSeekChat 客户端
    chat_client = DeepSeekChat()

    # 获取聊天响应
    system_message = "You are a helpful assistant"
    user_message = "Hello"
    response = chat_client.get_chat_response(system_message, user_message)

    # 打印响应内容
    print(response)
