import openai, os

from util.proxy import set_proxy

if __name__ == '__main__':
    set_proxy()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(os.getenv("OPENAI_API_KEY"))
    script_dir = os.path.dirname(os.path.realpath(__file__))

    audio_file = open(f"{script_dir}/data/podcast_clip.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript['text'])
