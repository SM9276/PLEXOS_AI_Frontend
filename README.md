# PLEXOS AI (RAG)

### First Step: Choosing A Large Language Model(LLM)
In this script, the llama 3.1 LLM was used with the help of Ollama to run the LLM locally. 
Go to https://ollama.com/ and install ollama 
Choose an LLM, run the following command in the terminan/cmd in order to download the LLM
        
    ollama pull llama3.1
To test, run the following and type a prompt:
    
    ollama run llama3.1 
### Second Step: Data
A folder named Extracted_Data contains the data that will be included in the Retrival Augmented Generation of the LLM.
### Third Step: RAG Script
Install the following dependencies: 
        
    pip install llama-index
    pip install llama-index-llms-ollama
    pip install llama_index.embeddings.huggingface

The RAG.py has two functions 

    construct_index()
        this function takes in a dirctory path, loads the files, then generates an index
        and saves it in the model Folder/Directory
    
    load_index()
        this function takes the model Folder/Directory from the storage returns it as an index
        
### Fourth Step: Run the flask website
install the following dependencies:
    
    pip install flask
run the app.py script which is a flask website that integrates the LLM model with the a website
then head to the page http://127.0.0.1:3000/views

first press the generate button, it will generate our model, everytime you start up the website press load model.
These buttons calls the RAG.py


