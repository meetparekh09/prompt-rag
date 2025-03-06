import numpy as np
import openai
import os
import faiss
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

reviews = [
    "I hate stories about backpacking. It's boring.",
    "A moving exploration of racial injustice and moral growth.",
    "Compelling dystopia, but overwhelmingly bleak.",
    "Timeless romance with sharp social commentary.",
    "Epic sea adventure with philosophical depth.",
    "Mesmerizing magic and romance with rich world-building.",
    "Beautifully descriptive, but predictable plot.",
    "A detailed and emotional journey through loss and art.",
    "Fresh take on greek mythology, but pacing dragged.",
    "Brilliant exploration of complex relationships and personal growth.",
    "Another bland romantic utopia. This time on tropical island."
]

def get_embedding(text):
    text = text.replace("\n", " ")
    return client.embeddings.create(
        input=text,
        model=os.getenv("OPENAI_EMBEDDING_MODEL")
    ).data[0].embedding
    

def index_reviews(reviews):
    vectors = [get_embedding(review) for review in reviews]

    index = faiss.IndexFlatL2(len(vectors[0]))
    
    vectors = np.array(vectors).reshape(len(vectors), -1)
    index.add(vectors)

    return index

def retrieve_reviews(index, query, reviews, k=2):
    query_vector = get_embedding(query)
    query_vector = np.array(query_vector).reshape(1, -1)

    distances, indices = index.search(query_vector, k)

    return [reviews[i] for i in indices[0]]


def predict_rating(book, related_reviews):
    reviews = "\n".join(related_reviews)

    prompt = (
        "Here is a book I might want to read:\n" +
        book + "\n\n" +

        "Here are relevant reviews from the past:\n" +
        reviews + "\n\n" +

        "On a scale of 1 (worst) to 5 (best), " +
        "how likely am I to enjoy this book? " +
        "Please respond with a single number between 1 and 5."
    )

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_CHAT_MODEL"),
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
    
    

index = index_reviews(reviews)
book = "The Beach by Alex Garland critiques backpacker culture by exposing the selfishness and moral decay behind heir pursuit of untouched paradise."

related_reviews = retrieve_reviews(index, book, reviews)

print(related_reviews)

rating = predict_rating(book, related_reviews)
print(f"Predicted rating: {rating}")
