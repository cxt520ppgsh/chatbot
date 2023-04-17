import openai
import json


def start():
    # 目前需要设置代理才可以访问 api
    # os.environ["HTTP_PROXY"] = "自己的代理地址"
    # os.environ["HTTPS_PROXY"] = "自己的代理地址"

    openai.api_key = "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"

    q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
            {"role": "user", "content": q}
        ]
    )
    print(rsp.get("choices")[0]["message"]["content"])


if __name__ == '__main__':
    start()
