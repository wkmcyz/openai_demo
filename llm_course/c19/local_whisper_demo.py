import whisper

from util.proxy import set_proxy

model = whisper.load_model("large")
index = 11  # number of fi


def transcript(clip, prompt, output):
    result = model.transcribe(clip, initial_prompt=prompt)
    with open(output, "w") as f:
        f.write(result['text'])
    print("Transcripted: ", clip)


if __name__ == '__main__':
    set_proxy()
    original_prompt = "这是一段Onboard播客，里面会聊到ChatGPT以及PALM这个大语言模型。这个模型也叫做Pathways Language Model。\n\n"
    prompt = original_prompt
    clip = f"./data/podcast_clip.mp3"
    output = f"./data/podcast_clip.txt"
    transcript(clip, prompt, output)
    # get last sentence of the transcript
    with open(output, "r") as f:
        transcript = f.read()
    sentences = transcript.split("。")
    prompt = original_prompt + sentences[-1]


    # for i in range(index):
    #     clip = f"./drive/MyDrive/colab_data/podcast/podcast_clip_{i}.mp3"
    #     output = f"./drive/MyDrive/colab_data/podcast/transcripts/local_podcast_clip_{i}.txt"
    #     transcript(clip, prompt, output)
    #     # get last sentence of the transcript
    #     with open(output, "r") as f:
    #         transcript = f.read()
    #     sentences = transcript.split("。")
    #     prompt = original_prompt + sentences[-1]
