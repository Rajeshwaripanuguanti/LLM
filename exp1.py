import gradio as gr
from transformers import pipeline
llm=pipeline("text-generation",model="gpt2")
def chatapp(query):
    response=llm(query,max_length=100)
    output=response[0]['generated_text']
    return response
gr.Interface(fn=chatapp,inputs="text",outputs="text").launch()
