# Necessary imports
import sys
import gradio as gr
import spaces

# Local imports
from src.config import (
    device,
    model_name,
    system_prompt,
    sampling,
    stream,
    top_p,
    top_k,
    temperature,
    repetition_penalty,
    max_new_tokens,
)
from src.app.model import load_model_and_tokenizer
from src.logger import logging
from src.exception import CustomExceptionHandling


# Model and tokenizer
model, tokenizer = load_model_and_tokenizer(model_name, device)


@spaces.GPU(duration=120)
def describe_image(image: str, question: str) -> str:
    """
    Generates an answer to a given question based on the provided image and question.

    Args:
        - image (str): The path to the image file.
        - question (str): The question text.

    Returns:
        str: The generated answer to the question.
    """
    try:
        # Check if image or question is None
        if not image or not question:
            gr.Warning("Please provide an image and a question.")

        # Message format for the model
        msgs = [{"role": "user", "content": [image, question]}]

        # Generate the answer
        answer = model.chat(
            image=None,
            msgs=msgs,
            tokenizer=tokenizer,
            sampling=sampling,
            stream=stream,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_tokens,
            system_prompt=system_prompt,
        )

        # Log the successful generation of the answer
        logging.info("Answer generated successfully.")

        # Return the answer
        return "".join(answer)

    # Handle exceptions that may occur during answer generation
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
