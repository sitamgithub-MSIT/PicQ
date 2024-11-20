# Importing the requirements
import warnings
warnings.filterwarnings("ignore")

import gradio as gr
from src.app.response import describe_image


# Image and text inputs for the interface
image = gr.Image(type="pil", label="Image")
question = gr.Textbox(label="Question", placeholder="Enter your question here")

# Output for the interface
answer = gr.Textbox(label="Predicted answer", show_label=True, show_copy_button=True)

# Examples for the interface
examples = [
    ["images/cat.jpg", "How many cats are there?"],
    ["images/dog.jpg", "¿De qué color es el perro?"],
    ["images/bird.jpg", "Que fait l'oiseau ?"],
]

# Title, description, and article for the interface
title = "Visual Question Answering"
description = "Gradio Demo for the MiniCPM-V 2.6 Vision Language Understanding and Generation model. This model can answer questions about images in natural language. To use it, simply upload your image, type a question, and click 'submit', or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://github.com/OpenBMB/MiniCPM-V' target='_blank'>Model GitHub Repo</a> | <a href='https://huggingface.co/openbmb/MiniCPM-V-2_6' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=describe_image,
    inputs=[image, question],
    outputs=answer,
    examples=examples,
    cache_examples=True,
    cache_mode="lazy",
    title=title,
    description=description,
    article=article,
    theme="JohnSmith9982/small_and_pretty",
    flagging_mode="never",
)
interface.launch(debug=False)
