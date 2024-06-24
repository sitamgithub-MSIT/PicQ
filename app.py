# Importing the requirements
import gradio as gr
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
import spaces

# Device for the model
device = "cuda"

# Load the model and tokenizer
model = AutoModel.from_pretrained(
    "openbmb/MiniCPM-Llama3-V-2_5", trust_remote_code=True, torch_dtype=torch.float16
)
model = model.to(device="cuda")
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


# Image and text inputs for the interface
image = gr.Image(type="pil", label="Image")
question = gr.Textbox(label="Question")

# Output for the interface
answer = gr.Textbox(label="Predicted answer")

# Examples for the interface
examples = [
    ["cat.jpg", "How many cats are there?"],
    ["dog.jpg", "What color is the dog?"],
    ["bird.jpg", "What is the bird doing?"],
]

# Title, description, and article for the interface
title = "Visual Question Answering"
description = "Gradio Demo for the MiniCPM Llama3 Vision Language Understanding and Generation model. This model can answer questions about images in natural language. To use it, simply upload your image and type a question and click 'submit', or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://github.com/OpenBMB/MiniCPM-V' target='_blank'>Model GitHub Repo</a> | <a href='https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=answer_question,
    inputs=[image, question],
    outputs=answer,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme="Soft",
    allow_flagging="never",
)
interface.launch(debug=False)
