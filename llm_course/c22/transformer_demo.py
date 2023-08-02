import time

import matplotlib.pyplot as plt
from transformers import TextGenerationPipeline

from util.proxy import set_proxy


def sentiment_analysis():
    from transformers import pipeline

    # device = 0 : gpu ; =1 : cpu
    # task : enumerate , 每一个 taks 返回不同的对象
    # model : 每个 task 有默认的 model . 具体的可选项，需要在 huggingface 上查看
    #   有的可以直接在线尝试 ：
    #       https://huggingface.co/runwayml/stable-diffusion-v1-5?text=a+ship+on+a+lake+by+picasso
    #       https://huggingface.co/openai/whisper-large-v2
    classifier = pipeline('sentiment-analysis', device=0)
    preds = classifier("I am really happy today!")
    print(preds)


def sentiment_analysis_chn():
    pass


def llama():
    from transformers import pipeline
    text_generation: TextGenerationPipeline = pipeline('text-generation', model="meta-llama/Llama-2-7b-chat-hf",
                                                       device=0)
    print("hhh")
    ans = text_generation("the light is on.")
    print(ans)


def stable_dif():
    from diffusers import DiffusionPipeline
    import torch
    # import cv2
    import cv2

    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16,
                                             use_safetensors=True, variant="fp16")
    pipe.to("cuda")

    # if using torch < 2.0
    # pipe.enable_xformers_memory_efficient_attention()
    pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead", fullgraph=True)

    prompt = "A princess with a crown"

    image = pipe(prompt=prompt).images[0]
    print(type(image))
    filename = time.time()
    image.save(f'{filename}.png')
    plt.imshow(image)
    plt.show()

if __name__ == '__main__':
    set_proxy()
    # sentiment_analysis()
    stable_dif()
