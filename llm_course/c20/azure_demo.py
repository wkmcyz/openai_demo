import os
import time

import azure.cognitiveservices.speech as speechsdk


def base_config():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'),
                                           region=os.environ.get('AZURE_SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    return speech_config, audio_config



# 音色见 https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#voice-styles-and-roles
def simple_demo(voice: int):
    # voice ==0 :xiaohan
    # voice == 1 : yunfeng
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    # The language of the voice that speaks.
    speech_config, audio_config = base_config()
    if voice == 0:
        speech_config.speech_synthesis_voice_name = 'zh-CN-XiaohanNeural'
    else:
        speech_config.speech_synthesis_voice_name = 'zh-CN-YunfengNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    text = "今天天气真不错，ChatGPT真好用。"

    speech_synthesizer.speak_text_async(text)
    time.sleep(100)


ssmls = [
    """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
               xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="zh-CN">
            <voice name="zh-CN-YunyeNeural">
                儿子看见母亲走了过来，说到：
                <mstts:express-as role="Boy" style="cheerful">
                    “妈妈，我想要买个新玩具”
                </mstts:express-as>
            </voice>
            <voice name="zh-CN-XiaomoNeural">
                母亲放下包，说：
                <mstts:express-as role="SeniorFemale" style="angry">
                    “我看你长得像个玩具。”
                </mstts:express-as>
            </voice>
        </speak>""",

    """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
           xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
        <voice name="en-US-JennyNeural">
            <mstts:express-as style="excited">
                That'd be just amazing!
            </mstts:express-as>
            <mstts:express-as style="friendly">
                What's next?
            </mstts:express-as>
        </voice>
    </speak>"""

]


def azure_special_sound_demo(ssml: str):
    speech_config, audio_config = base_config()
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()
    stream = speechsdk.AudioDataStream(speech_synthesis_result)
    stream.save_to_wav_file("./data/azure_special_sound_demo_tts.mp3")


if __name__ == '__main__':
    # simple_demo(0)
    # simple_demo(1)
    azure_special_sound_demo(ssmls[1])
