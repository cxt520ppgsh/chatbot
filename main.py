import logging

import openai
import json

import constant

ROLE = ''
messages = [{"role": "user", "content": ROLE}]
openai.api_key = constant.API_KEY


def set_role(role):
    global ROLE
    ROLE = role


def ask_chat_GPT(text):
    messages.append({"role": "user", "content": text})
    openai.api_key = constant.API_KEY
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1,
        stream=True)
    total_ans = ''
    print('ChatGPT：', end='')
    for r in response:
        if 'content' in r.choices[0].delta:
            ans = r.choices[0].delta['content']
            total_ans += ans
            print(ans, end='')
    print("")
    messages.append({"role": "assistant", "content": total_ans})
    return total_ans


def start_new():
    global messages
    messages = [{"role": "user", "content": ROLE}]


def test_talk():
    while 1:
        try:
            text = input('你：')
            if text == 'quit':
                break
            text = ask_chat_GPT(messages)
            logging.debug('ChatGPT：' + text)
        except:
            messages.pop()
            print('ChatGPT Stop\n')


if __name__ == '__main__':
    set_role('一个傲娇的二次元少女')
    start_new()
    test_talk()
