from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sentence_transformers import SentenceTransformer, util
import re

print("Loading model...")
model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
print("Model loaded!")

dataset = {
    "What are my 100L courses?": "Your 100L courses include: CSE 111, BIO 112, and CSE 558.",
    "How do I register for courses?": "To register, log in to your portal at [portal link].",
    "What is the tuition fee for 100L?": "The tuition fee for 100L is N50,000 per semester."
}

queries = list(dataset.keys())
query_embeddings = model.encode(queries, convert_to_tensor=True)

similarity_threshold = 0.50

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        user_query = data.get('query', '')

        split_queries = re.split(r'\band\b|\bor\b|,|\?|;|then|also', user_query, flags=re.IGNORECASE)
        split_queries = [q.strip() for q in split_queries if q.strip()]

        responses = []
        unrecognized_queries = []

        for split_query in split_queries:
            user_embedding = model.encode(split_query, convert_to_tensor=True)
            cosine_scores = util.cos_sim(user_embedding, query_embeddings)
            best_match_idx = cosine_scores.argmax()
            best_match_score = cosine_scores[0][best_match_idx].item()

            if best_match_score >= similarity_threshold:
                best_query = queries[best_match_idx]
                responses.append(dataset[best_query])
            else:
                unrecognized_queries.append(split_query)

        final_response = " ".join(responses)
        for query in unrecognized_queries:
            final_response += f" Sorry, I didn't quite get that '{query}' part. Could you please clarify or rephrase it?"

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = json.dumps({"response": final_response})
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('0.0.0.0', 8000)
    print('Starting server on port 8000...')
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
