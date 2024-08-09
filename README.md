# PLEXOS AI (RAG)

### First Step: Setting up the enviorment
Go to https://ollama.com/ and install ollama, Run the following command to install llama3.1 LLM:

    ollama pull llama3.1
To test and interact with the LLM, run the following and type a prompt:
    
    ollama run llama3.1 
Create a enviorment using the following command
    
    conda create -n "plexosAI" python
Then run follow the following to activate the enviorment

    conda activate plexosAI
Once the enviorment is active install the following dependencies: 

    pip install llama-index
    pip install llama-index-llms-ollama
    pip install llama_index.embeddings.huggingface
    pip install flask

### Second Step: Data
A folder named Extracted_Data contains the data that will be included in the Retrival Augmented Generation of the LLM.
### Third Step: RAG Script
The RAG.py has two functions 

    construct_index()
        this function takes in a dirctory path, loads the files, then generates an index
        and saves it in the model Folder/Directory
    
    load_index()
        this function takes the model Folder/Directory from the storage returns it as an index
        
### Fourth Step: Run the flask website
run the app.py script which is a flask website that integrates the LLM model with the a website
then head to the page http://127.0.0.1:3000/views

first press the generate button, it will generate our model, everytime you start up the website press load model.
These buttons calls the RAG.py


