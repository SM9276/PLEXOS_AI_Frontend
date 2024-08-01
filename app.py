from flask import Flask, jsonify, request
from views import views
from RAG import load_index, construct_index

# Initialize the Flask web application
app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")  # Register the 'views' blueprint with the app

index = None  # A global variable to store an index, initially set to None


@app.route('/callLoad')
def callLoadIndex():
    """
    This function is called when the '/callLoad' URL is accessed.

    It loads an index using the 'load_index' function from the RAG module and updates the global 'index' variable.

    Returns:
        A JSON response indicating that the index was loaded successfully, along with a status code of 200 (OK).
    """
    global index
    index = load_index()
    return jsonify({"message": "Index loaded successfully"}), 200


@app.route('/callGenerate')
def callGenerateIndex():
    """
    This function is called when the '/callGenerate' URL is accessed.

    It creates a new index using the 'construct_index' function from the RAG module, based on the contents of a directory called "Extracted_Data", and updates the global 'index' variable.

    Returns:
        A JSON response indicating that the index was constructed successfully, along with a status code of 200 (OK).
    """
    global index
    index = construct_index(directory_path="Extracted_Data")
    return jsonify({"message": "Index constructed successfully"}), 200


@app.route('/query', methods=['POST'])
def queryIndex():
    """
    This function handles POST requests to the '/query' URL.

    It takes a JSON payload with a 'prompt' field, queries the index using this prompt, and returns the result.

    If the index is not loaded or constructed, or if the 'prompt' is missing, it returns an error message.

    Returns:
        A JSON response with the query result if successful, or an error message if something goes wrong.
    """
    global index
    if index is None:
        return jsonify({"error": "Index not loaded or constructed"}), 400

    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt not provided"}), 400

    try:
        query_engine = index.as_query_engine()
        response = query_engine.query(prompt)
        print(response)
        # Assuming response has a method to get a JSON serializable representation
        response_data = convert_response_to_serializable(response)

        return jsonify({"response": response_data}), 200

    except Exception as e:
        app.logger.error(f"Error querying index: {e}")
        return jsonify({"error": "Failed to process query"}), 500


def convert_response_to_serializable(response):
    """
    Converts a query response into a format that can be easily converted to JSON.

    This is a placeholder implementation; it needs to be customized based on the actual response format.

    Args:
        response: The query response to convert.

    Returns:
        A serializable version of the response, or a string if conversion fails.
    """
    if hasattr(response, 'to_dict'):
        return response.to_dict()  # Example conversion to dictionary
    return str(response)  # Fallback to string representation


if __name__ == '__main__':
    # Run the Flask web application on port 3000
    app.run(debug=False, port=3000)
