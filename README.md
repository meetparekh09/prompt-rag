# Prompt RAG Application

## Overview
This application demonstrates the use of Retrieval-Augmented Generation (RAG) to enhance the quality of AI-generated responses by providing relevant context dynamically. The system predicts a user's book rating based on their previous reviews, using embedding-based similarity search to find the most relevant past reviews.

## Dynamic Context in Prompt Engineering

Dynamic context refers to the practice of adaptively selecting and incorporating relevant information into prompts based on the specific query or task at hand. Rather than using static, pre-defined prompts, dynamic context:

- Tailors the prompt to each specific query
- Reduces hallucinations by grounding responses in relevant data
- Improves response quality by providing the AI with the most pertinent information
- Enables more personalized and accurate responses

## How RAG is Leveraged

Retrieval-Augmented Generation (RAG) combines the power of retrieval systems with generative AI models to produce more accurate and contextually relevant responses:

1. **Retrieval**: The system searches a database of information to find content relevant to the current query
2. **Augmentation**: The retrieved information is incorporated into the prompt
3. **Generation**: The AI model generates a response based on both the query and the retrieved context

In this application, RAG is used to:
- Retrieve past book reviews that are semantically similar to a new book description
- Augment the prompt with these relevant reviews
- Generate a predicted rating based on the user's past preferences

## Embedding-Based Retrieval

This application uses vector embeddings rather than traditional lexical search methods:

- **Embeddings**: Text is converted into dense vector representations that capture semantic meaning
- **Similarity Search**: FAISS (Facebook AI Similarity Search) is used to efficiently find the most similar vectors
- **Advantages over lexical search**: 
  - Captures semantic similarity rather than just keyword matching
  - Understands conceptual relationships between texts
  - Can find relevant content even when different terminology is used

## Running Locally

### Prerequisites
- Docker installed on your system
- OpenAI API key

### Setup
1. Clone this repository
2. Create a `.env` file with your OpenAI API credentials:
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_EMBEDDING_MODEL=text-embedding-3-small
   OPENAI_CHAT_MODEL=gpt-4o-mini
   ```

### Running with Docker
1. Build the Docker image:
   ```
   make build
   ```

2. Run the application:
   ```
   make run
   ```

3. To access a shell inside the container:
   ```
   make exec
   ```

4. To clean up and remove the Docker image:
   ```
   make clean
   ```

The application will process the sample book reviews and provide a predicted rating based on the semantic similarity between the new book description and past reviews.

