from util.proxy import timeit


@timeit
def local_model_demo():
    # Following pip packages need to be installed:
    # !pip install git+https://github.com/huggingface/transformers sentencepiece datasets

    from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
    import torch
    import soundfile as sf
    from datasets import load_dataset
    """
    
SpeechT5Processor.from_pretrained用于加载预训练的处理器，用于将文本转换为模型可以理解的输入格式。
SpeechT5ForTextToSpeech.from_pretrained用于加载预训练的SpeechT5文字转语音模型。
SpeechT5HifiGan.from_pretrained用于加载预训练的HiFIGAN声码器，它可以将模型生成的声谱转换为可听的音频波形。
"""
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    # processor将给定的文本"Hello, my dog is cute"转换为模型可以接受的输入张量。
    inputs = processor(text="Hello, my dog is cute", return_tensors="pt")

    # 使用load_dataset从指定的数据集中加载说话人的声音特性（称为xvector）。这些嵌入可以使生成的语音具有特定的说话人特点。
    # 具体包含哪些说话人以及各自该如何索引到，可以参考 https://huggingface.co/datasets/Matthijs/cmu-arctic-xvectors¢
    # load xvector containing speaker's voice characteristics from a dataset
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    # 可以通过 embeddings_dataset[7306].filename 来查看这个说话人的声音信息。
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    # 使用model.generate_speech方法生成语音。这个方法接收输入ID、说话人嵌入以及声码器，并返回一段音频波形。
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

    sf.write("speech.wav", speech.numpy(), samplerate=16000)


if __name__ == '__main__':
    local_model_demo()
