from sentence_transformers import SentenceTransformer, util
import re
import sys
#import os
#os.environ["TRANSFORMERS_OFFLINE"] = "1"

# Initialize model all-MiniLM-L4-v2
#model = SentenceTransformer('all-MiniLM-L6-v2-main')

model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

# Dataset: Questions and Answers
dataset = {
    "What are my 100L courses?": "Your 100L courses include: CSE 111, BIO 112, and CSE 558.",
    "How do I register for courses?": "To register, log in to your portal at [portal link].",
    "What is the tuition fee for 100L?": "The tuition fee for 100L is N50,000 per semester."
}

# Precompute embeddings for dataset
queries = list(dataset.keys())
query_embeddings = model.encode(queries, convert_to_tensor=True)

# Get the user query passed from PHP as a command-line argument
user_query = sys.argv[1] if len(sys.argv) > 1 else ""
with open("debug_python_input.txt", "w", encoding="utf-8") as f:
    f.write(user_query)

# Split the user query into multiple questions based on common connectors and punctuation (e.g., "and", "or", commas, semicolons, "then")
split_queries = re.split(r'\band\b|\bor\b|,|\?|;|then|also', user_query, flags=re.IGNORECASE)

# Clean up any empty queries from the split
split_queries = [query.strip() for query in split_queries if query.strip()]

# List to store responses for each question
responses = []
unrecognized_queries = []  # Track unrecognized questions
understood_all = True  # Track if there are any unrecognized queries

# Define a threshold for similarity (e.g., 0.50 for 50%)
similarity_threshold = 0.50

# Process each split query
for split_query in split_queries:
    # Encode the query
    user_embedding = model.encode(split_query, convert_to_tensor=True)

    # Find closest match
    cosine_scores = util.cos_sim(user_embedding, query_embeddings)

    # Find the best match index based on maximum cosine similarity
    best_match_idx = cosine_scores.argmax()

    # Get the cosine similarity score for the best match
    best_match_score = cosine_scores[0][best_match_idx].item()

    if best_match_score >= similarity_threshold:
        # If the best match score is above the threshold, return the response
        best_query = queries[best_match_idx]
        responses.append(f"{dataset[best_query]}")
    else:
        # If the similarity score is below the threshold, mark it as unrecognized
        understood_all = False
        unrecognized_queries.append(split_query)

# Combine the responses into a single output
final_response = " ".join([resp for resp in responses if resp])  # Ignore None values

# If there was an unrecognized question, add the clarification message at the end
if unrecognized_queries:
    # Add apology for each unrecognized query
    for query in unrecognized_queries:
        final_response += f" Sorry, I didn't quite get that '{query}' part. Could you please clarify or rephrase it?"

# Print the final response
print(final_response)
