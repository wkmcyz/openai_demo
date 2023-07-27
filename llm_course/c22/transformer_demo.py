from transformers import pipeline

if __name__ == '__main__':
    # import torch
    # print(torch.__version__)
    # print(torch.cuda.is_available())
    classifier = pipeline('sentiment-analysis',device=0)
    preds = classifier("I am really happy today!")
    print(preds)
