from src.gpt.main import ask_chat_gpt_not_stream, set_role, start_new
from src.stt.iat_ws_python3 import main_stt


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
    # main_stt()
    set_role('你是一个二次元傲娇少女，用这样的语气讲话')
    start_new()
    test_talk()
