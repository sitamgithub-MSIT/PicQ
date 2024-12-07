# Necessary imports
import os
import sys
from dotenv import load_dotenv
from typing import Any
import torch
from transformers import AutoModel, AutoTokenizer, AutoProcessor

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


# Load the Environment Variables from .env file
load_dotenv()

# Access token for using the model
access_token = os.environ.get("ACCESS_TOKEN")


def load_model_tokenizer_and_processor(model_name: str, device: str) -> Any:
    """
    Load the model, tokenizer and processor.

    Args:
        - model_name (str): The name of the model to load.
        - device (str): The device to load the model onto.

    Returns:
        - model: The loaded model.
        - tokenizer: The loaded tokenizer.
        - processor: The loaded processor.
    """
    try:
        # Load the model, tokenizer and processor
        model = AutoModel.from_pretrained(
            model_name,
            trust_remote_code=True,
            attn_implementation="sdpa",
            torch_dtype=torch.bfloat16,
            token=access_token
        )
        model = model.eval().to(device=device)
        tokenizer = AutoTokenizer.from_pretrained(
            model_name, trust_remote_code=True, token=access_token
        )
        processor = AutoProcessor.from_pretrained(
            model_name, trust_remote_code=True, token=access_token
        )

        # Log the successful loading of the model, tokenizer and processor
        logging.info("Model, tokenizer and processor loaded successfully.")

        # Return the model, tokenizer and processor
        return model, tokenizer, processor

    # Handle exceptions that may occur during model, tokenizer and processor loading
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
