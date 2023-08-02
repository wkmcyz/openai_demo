from util.proxy import set_proxy


def f():
    import os, requests, json

    API_TOKEN = os.environ.get("HUGGINGFACE_API_KEY")

    # model = "google/flan-t5-xxl"
    model = "meta-llama/Llama-2-70b-chat-hf"
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

    def query(payload, api_url=API_URL, headers=headers):
        data = json.dumps(payload)
        response = requests.request("POST", api_url, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))

    # question = "Please answer the following question. What is the capital of France?"
    question = "Plean answer the following question. In songs,what is the next sequence of 'Welcome to California'"
    data = query({"inputs": question})

    print(data)


if __name__ == '__main__':
    set_proxy()
    f()