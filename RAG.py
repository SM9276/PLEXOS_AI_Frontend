from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


def construct_index(directory_path):
    """
    Constructs a new index using documents from a specified directory.

    This function sets up the language model and embedding model, reads documents from a directory,
    and builds an index that can be used for querying. The constructed index is saved for future use.

    Args:
        directory_path (str): The path to the directory containing documents to be indexed.

    Returns:
        VectorStoreIndex: The constructed index containing the documents.
    """
    # Set up language model and embedding model settings
    Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # Load documents from the specified directory
    documents = SimpleDirectoryReader(directory_path).load_data()

    # Create a storage context and construct the index
    storage_context = StorageContext.from_defaults()
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        show_progress=True
    )

    # Save the storage context for future use
    storage_context.persist(persist_dir='model')
    print("Construction Complete!")
    return index


def load_index():
    """
    Loads a previously saved index from storage.

    This function retrieves the last saved index, allowing for querying or further operations
    without needing to reconstruct the index from the original documents.

    Returns:
        VectorStoreIndex: The loaded index ready for querying.
    """
    print("Loading last model ...")
    # Set up language model and embedding model settings
    Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    # Create a storage context and load the index from storage
    storage_context = StorageContext.from_defaults(persist_dir='model')
    index = load_index_from_storage(storage_context=storage_context)
    print("Loading Complete!")
    return index

# Uncomment one of the following lines to construct or load an index:
# ChatIndex = construct_index(directory_path="Extracted_Data")
# ChatIndex = load_index()
