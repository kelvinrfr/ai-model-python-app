import requests
import json

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    
    prompt = prompt + (
        " Rules for response:"
        " 1) Be as concise as possible. No more than 70 words."
        " 2) Fit answer in one paragraph."
        " 3) Use a formal tone."
        " 4) Be funny."
    )

    data = {
        "model": "llama3.1:latest",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        return result['response']
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")

# Main execution
if __name__ == "__main__":
    question = "Why sky is blue?"
    answer = ask_ollama(question)
    print(f"Question: {question}")
    print(f"Answer: {answer}")