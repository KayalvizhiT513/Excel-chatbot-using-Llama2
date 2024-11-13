from huggingface_hub import hf_hub_download

# Replace with the repository/model name and filename
model_path = hf_hub_download(
    repo_id="TheBloke/Llama-2-7b-Chat-GGML",
    filename="llama-2-7b-chat.ggmlv3.q4_1.bin",
    cache_dir="res"  # Downloads to the 'res' directory
)
print(f"Model downloaded to {model_path}")
