# Model settings
device = "cuda"
model_name = "openbmb/MiniCPM-V-2_6"

# Decoding settings
sampling = True
stream = True
top_p = 0.8
top_k = 100
temperature = 0.7
repetition_penalty = 1.05
max_new_tokens = 2048

# System Prompt
system_prompt = """
You are an AI assistant specialized in visual content analysis.
Given an image and a related question, analyze the image thoroughly and provide a precise and informative answer based on the visible content.
Ensure your response is clear, accurate, and directly addresses the question.
"""
