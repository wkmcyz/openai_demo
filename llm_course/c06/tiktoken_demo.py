import tiktoken

from llm_course.c06.conversation_calc_token import Conversation2
from util.proxy import set_proxy

if __name__ == '__main__':
    set_proxy()
    encoding = tiktoken.get_encoding("cl100k_base")

    prompt = """你是一个中国厨师，用中文回答做菜的问题。你的回答需要满足以下要求。
    1. 你的回答必须是中文
    2. 回答需要限制在100个字之内"""
    conv2 = Conversation2(prompt, 3)
    question1 = "你是谁？"
    answer1, num_of_tokens = conv2.ask(question1)
    print("总共消耗的token数量是 : %d" % (num_of_tokens))

    prompt_count = len(encoding.encode(prompt))
    question1_count = len(encoding.encode(question1))
    answer1_count = len(encoding.encode(answer1))
    total_count = prompt_count + question1_count + answer1_count
    print("Prompt消耗 %d Token, 问题消耗 %d Token，回答消耗 %d Token，总共消耗 %d Token" % (
        prompt_count, question1_count, answer1_count, total_count))
