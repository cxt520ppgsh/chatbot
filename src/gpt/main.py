import logging

import openai
import json

import constant

ROLE = '你只是一个打工仔'
messages = [{"role": "system", "content": ROLE}]
openai.api_key = constant.CHAT_API_KEY


def set_role(role):
    global ROLE, messages
    ROLE = role


def ask_chat_gpt_with_stream(text):
    messages.append({"role": "user", "content": text})
    openai.api_key = constant.CHAT_API_KEY
    response = openai.ChatCompletion.create(
        model=constant.CHAT_MODEL,
        messages=messages,
        temperature=constant.CHAT_TEMPERATURE,
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
        model=constant.CHAT_MODEL,
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
