import logging

import openai
import json

import constant

ROLE = '你只是一个打工仔'
messages = [{"role": "system", "content": ROLE}]
openai.api_key = constant.API_KEY
MODEL = "gpt-3.5-turbo"


def set_role(role):
    global ROLE, messages
    ROLE = role


def ask_chat_gpt_with_stream(text):
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


def ask_chat_gpt_not_stream(text):
    messages.append({"role": "user", "content": text})
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=1,
        stream=False)
    anser = response.get("choices")[0]["message"]["content"]
    messages.append({"role": "assistant", "content": anser})

    print('ChatGPT：', anser)
    return anser


def start_new():
    global messages
    messages = [{"role": "system", "content": ROLE}]


def test_talk():
    while 1:
        try:
            text = input('你：')
            if text == 'quit':
                break
            ask_chat_gpt_not_stream(text)
        except Exception as e:
            print('ChatGPT Stop', e.args)


if __name__ == '__main__':
    set_role('你是一个二次元傲娇少女，用这样的语气讲话')
    start_new()
    test_talk()
