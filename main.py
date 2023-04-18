import logging

import openai
import json

import constant

ROLE = ''


def set_config():
    openai.api_key = constant.API_KEY


def set_role(role):
    global ROLE
    ROLE = role


def askChatGPT(messages):
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
    return total_ans


def main():
    messages = [{"role": "user", "content": ROLE}]
    while 1:
        try:
            text = input('你：')
            if text == 'quit':
                break

            d = {"role": "user", "content": text}
            messages.append(d)

            text = askChatGPT(messages)
            d = {"role": "assistant", "content": text}
            logging.debug('ChatGPT：' + text)
            messages.append(d)
        except:
            messages.pop()
            print('ChatGPT Stop\n')


if __name__ == '__main__':
    set_role('')
    main()
