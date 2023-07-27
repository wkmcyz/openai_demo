from util.proxy import set_proxy


# display some images
def display_images(images):
    fig, axes = plt.subplots(1, 5, figsize=(15, 6))
    axes = axes.ravel()

    for idx, img in enumerate(images):
        axes[idx].imshow(img)
        axes[idx].axis('off')

    plt.subplots_adjust(wspace=-1.2, hspace=0.2)
    plt.show()




if __name__ == '__main__':
    set_proxy()
    # load datasets
    from datasets import load_dataset

    dataset = load_dataset("rajuptvs/ecommerce_products_clip")

    import matplotlib.pyplot as plt

    training_split = dataset["train"]

    images = [example["image"] for example in training_split.select(range(9))]
    # display_images(images)

    import torch
    import torchvision.transforms as transforms
    from PIL import Image
    from datasets import load_dataset
    from transformers import CLIPProcessor, CLIPModel

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


    def get_image_features(image):
        with torch.no_grad():
            inputs = processor(images=[image], return_tensors="pt", padding=True)
            inputs.to(device)
            features = model.get_image_features(**inputs)
        return features.cpu().numpy()


    def add_image_features(example):
        example["features"] = get_image_features(example["image"])
        return example


    # Apply the function to the training_split
    training_split = training_split.map(add_image_features)

    # 得到的 features 包含图片 feature 向量

    # add to faiss

    import numpy as np
    import faiss

    features = [example["features"] for example in training_split]
    features_matrix = np.vstack(features)

    dimension = features_matrix.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(features_matrix.astype('float32'))












    # search

    def get_text_features(text):
        with torch.no_grad():
            inputs = processor(text=[text], return_tensors="pt", padding=True)
            inputs.to(device)
            features = model.get_text_features(**inputs)
        return features.cpu().numpy()


    def search(query_text, top_k=5):
        # Get the text feature vector for the input query
        text_features = get_text_features(query_text)

        # Perform a search using the FAISS index
        distances, indices = index.search(text_features.astype("float32"), top_k)

        # Get the corresponding images and distances
        results = [
            {"image": training_split[i]["image"], "distance": distances[0][j]}
            for j, i in enumerate(indices[0])
        ]

        return results


    query_text = "A red dress"
    results = search(query_text)


    # Display the search results
    def display_search_results(results):
        fig, axes = plt.subplots(1, len(results), figsize=(15, 5))
        axes = axes.ravel()

        for idx, result in enumerate(results):
            axes[idx].imshow(result["image"])
            axes[idx].set_title(f"Distance: {result['distance']:.2f}")
            axes[idx].axis('off')

        plt.subplots_adjust(wspace=0.2, hspace=0.2)
        plt.show()


    display_search_results(results)


