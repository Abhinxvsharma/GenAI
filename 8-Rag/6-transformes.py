# Transformers is a library developed by Hugging Face that provides state-of-the-art pre-trained models for natural language processing (NLP) tasks. It allows you to easily use these models for various applications such as text classification, text generation, question answering, and more.

# In this example, we will demonstrate how to use the Transformers library for sentiment analysis and text generation.  

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I love learning AI and Machine Learning!")

print(result)


# ************** Text Generation Example *****************

# from transformers import pipeline

# generator = pipeline(
#     "text-generation",
#     model="gpt2"
# )

# result = generator(
#     "Artificial Intelligence is",
#     max_length=50,
#     num_return_sequences=1
# )

# print(result[0]["generated_text"])