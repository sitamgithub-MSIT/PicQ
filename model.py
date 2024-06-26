# Importing the requirements
import torch
from transformers import AutoModel, AutoTokenizer
import spaces


# Device for the model
device = "cuda"

# Load the model and tokenizer
model = AutoModel.from_pretrained(
    "openbmb/MiniCPM-Llama3-V-2_5", trust_remote_code=True, torch_dtype=torch.float16
)
model = model.to(device=device)
tokenizer = AutoTokenizer.from_pretrained(
    "openbmb/MiniCPM-Llama3-V-2_5", trust_remote_code=True
)
model.eval()


@spaces.GPU(duration=120)
def answer_question(image, question):
    """
    Generates an answer to a given question based on the provided image and question.
    Args:
        image (str): The path to the image file.
        question (str): The question text.
    Returns:
        str: The generated answer to the question.
    """

    # Message format for the model
    msgs = [{"role": "user", "content": question}]

    # Generate the answer
    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        sampling=True,
        temperature=0.7,
        stream=True,
        system_prompt="You are an AI assistant specialized in visual content analysis. Given an image and a related question, analyze the image thoroughly and provide a precise and informative answer based on the visible content. Ensure your response is clear, accurate, and directly addresses the question.",
    )

    # Return the answer
    return "".join(res)
