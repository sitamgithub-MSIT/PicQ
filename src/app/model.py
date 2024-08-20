# Necessary imports
import sys
from typing import Any
import torch
from transformers import AutoModel, AutoTokenizer

# Local imports
from src.logger import logging
from src.exception import CustomExceptionHandling


def load_model_and_tokenizer(model_name: str, device: str) -> Any:
    """
    Load the model and tokenizer.

    Args:
        - model_name (str): The name of the model to load.
        - device (str): The device to load the model onto.

    Returns:
        - model: The loaded model.
        - tokenizer: The loaded tokenizer.
    """
    try:
        # Load the model and tokenizer
        model = AutoModel.from_pretrained(
            model_name,
            trust_remote_code=True,
            attn_implementation="sdpa",
            torch_dtype=torch.bfloat16,
        )
        model = model.to(device=device)
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model.eval()

        # Log the successful loading of the model and tokenizer
        logging.info("Model and tokenizer loaded successfully.")

        # Return the model and tokenizer
        return model, tokenizer

    # Handle exceptions that may occur during model and tokenizer loading
    except Exception as e:
        # Custom exception handling
        raise CustomExceptionHandling(e, sys) from e
