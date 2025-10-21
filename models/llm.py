# Konfigurasi dan wrapper LLM untuk chatbot
from transformers import pipeline

class LLMModel:
    def __init__(self, model_name='gpt2'):
        self.pipeline = pipeline('text-generation', model=model_name)

    def chat(self, prompt):
        return self.pipeline(prompt, max_length=256)[0]['generated_text']
