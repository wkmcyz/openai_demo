from llama_index import download_loader, GPTVectorStoreIndex, ServiceContext, StorageContext, load_index_from_storage
from pathlib import Path

years = [2022, 2021, 2020, 2019]
UnstructuredReader = download_loader("UnstructuredReader", refresh_cache=True)

loader = UnstructuredReader()
doc_set = {}
all_docs = []
for year in years:
    print("loading year: ", year)
    year_docs = loader.load_data(file=Path(f'./data/UBER/UBER_{year}.html'), split_documents=False)
    # insert year metadata into each year
    for d in year_docs:
        d.extra_info = {"year": year}
    doc_set[year] = year_docs
    all_docs.extend(year_docs)

# initialize simple vector indices + global vector index
service_context = ServiceContext.from_defaults(chunk_size=512)
index_set = {}
for year in years:
    print("building index for year: ", year)
    storage_context = StorageContext.from_defaults()
    cur_index = GPTVectorStoreIndex.from_documents(
        doc_set[year],
        service_context=service_context,
        storage_context=storage_context,
    )
    index_set[year] = cur_index
    print("persisting index for year: ", year)
    storage_context.persist(persist_dir=f'./storage/{year}')


# Load indices from disk
index_set = {}
for year in years:
    storage_context = StorageContext.from_defaults(persist_dir=f'./storage/{year}')
    cur_index = load_index_from_storage(storage_context=storage_context)
    index_set[year] = cur_index

