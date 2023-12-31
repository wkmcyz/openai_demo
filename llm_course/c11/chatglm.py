# pip install icetk
# pip install cpm_kernels
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from llama_index import SimpleDirectoryReader, LangchainEmbedding, ServiceContext, GPTVectorStoreIndex
from llama_index.node_parser import SimpleNodeParser
from transformers import AutoTokenizer, AutoModel

from util.proxy import set_proxy

if __name__ == '__main__':
    set_proxy()
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
    # model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half()
    model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
    model = model.eval()
    # 使用 CPU 运行
    # model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4",trust_remote_code=True).float()
    # input
    text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=100, chunk_overlap=20)
    parser = SimpleNodeParser(text_splitter=text_splitter)
    documents = SimpleDirectoryReader('./data/faq/').load_data()
    nodes = parser.get_nodes_from_documents(documents)

    # embedding model
    service_context = ServiceContext.from_defaults(embed_model=model)

    # to index
    index = GPTVectorStoreIndex(nodes=nodes, service_context=service_context)
    #
    query_engine = index.as_query_engine()
    # 我们是一家专注于提供优质服装和配饰的网上零售商。
    s = query_engine.query("你们是做什么的？")
    print("s:")
    print(s)
