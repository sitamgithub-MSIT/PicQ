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
