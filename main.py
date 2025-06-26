from flask import Flask, request, jsonify, render_template
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv("secret.env")

# Access the API key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")


# Check if the API key is available
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is missing")


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return "Flask API is working!"

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ask_query', methods=['POST'])
def ask_query():
    try:
        data = request.get_json()
        query = data.get('query')
        generated_content = data.get('generated_content')

        if not query or not generated_content:
            return jsonify({'error': 'Missing query or generated content'}), 400

        full_prompt = f"""You are an AI assistant. Based on the following article, answer the user's question.
        
        Article: {generated_content}

        Question: {query}

        Answer:"""

        prompt_template = PromptTemplate.from_template(full_prompt)
        llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=google_api_key)
        chain = LLMChain(llm=llm, prompt=prompt_template)

        response = chain.run({})
        return jsonify({'answer': response})

    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return jsonify({'error': f'Internal Server Error: {str(e)}'}), 500

@app.route('/prompts')
def prompts():
    return render_template('prompts.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        print("Request Headers:", request.headers)

        # Ensure JSON content-type
        if not request.is_json:
            return jsonify({'error': 'Request must be in JSON format'}), 400

        # Parse JSON
        data = request.get_json()
        print("Received Data:", data)

        prompt_input = data.get('prompt')
        tone = data.get('tone', 'informative')
        audience = data.get('audience', 'general')
        length = data.get('length', 'concise')

        if not prompt_input:
            return jsonify({'error': 'Prompt cannot be empty'}), 400

        modified_prompt = f"Generate a {tone} article for a {audience} audience with a {length} length on the topic: {prompt_input}. Make sure to provide an apt title and adhere to the mentioned style"

        # Create LangChain components
        prompt_template = PromptTemplate.from_template(modified_prompt)
       # Initialize the LLM with the API key
        llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key=google_api_key)
        chain = LLMChain(llm=llm, prompt=prompt_template)

        # Generate the output
        output = chain.run({"title": prompt_input})
        print("Generated Output:", output)

        return jsonify({'output': output})

    except Exception as e:
        import traceback
        print(traceback.format_exc())  # Log error for debugging
        return jsonify({'error': f'Internal Server Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
