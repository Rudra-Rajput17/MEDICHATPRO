import modal

# Create a Modal App
stub = modal.App("medichatpro_gpu")

# Remote FAISS index creation on GPU
@stub.function(gpu="H100", timeout=3600)
def create_index_modal(chunks):
    from app.vectorstore_utils import create_faiss_index
    return create_faiss_index(chunks)

# Remote chat model call on GPU
@stub.function(gpu="H100", timeout=3600)
def ask_model_modal(system_prompt):
    from app.chat_utils import get_chat_model, ask_chat_model
    from app.config import EURI_API_KEY

    chat_model = get_chat_model(api_key=EURI_API_KEY)
    response = ask_chat_model(chat_model, system_prompt)
    return response
