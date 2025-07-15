from transformers import AutoTokenizer,AutoModelForCausalLM
import torch
model_name="TinyLlama/TinyLlama-1.1B-chat-v1.0"
tokenizer=AutoTokenizer.from_pretrained(model_name)
model=AutoModelForCausalLM.from_pretrained(model_name)
prompt="Defination of python LLM"
inputs=tokenizer(prompt,return_tensors="pt")
outputs=model.generate(**inputs,max_new_tokens=30)
response=tokenizer.decode(outputs[0],skip_special_tokens=True)
print(response)
prompt="""Question:What is Ai?
Answer:AI is machine can tbhink like a human
Question:what is ML?
Answer:"""
inputs=tokenizer(prompt,return_tensors="pt")
outputs=model.generate(**inputs,max_new_tokens=30)
response=tokenizer.decode(outputs[0])
print(response)

#few shot prompt technique
prompt="""Correct the grammer:
Incorrect:he go to school every day
correct:he goes to school everyday
Incorrect:she don't like apples
correct:she doesn't like apples"""
inputs=tokenizer(prompt,return_tensors="pt")
outputs=model.generate(**inputs,max_new_tokens=30)
response=tokenizer.decode(outputs[0],skip_special_tokens=True)
print(response)




#change of thought(CoT)
prompt="""A train travels 60km in 1 hour and 30km in the next 0.5 hours.
          what is its average speed"""
inputs=tokenizer(prompt,return_tensors="pt")
outputs=model.generate(**inputs,max_new_tokens=100,do_sample=True)
response=tokenizer.decode(outputs[0])
print(response)


#role prompting
prompt="<|system|>you are a helpful English teacher.<|user|>what is diff between affect and effect"
inputs=tokenizer(prompt,return_tensors="pt")
outputs=model.generate(**inputs,max_new_tokens=100,do_sample=True)
response=tokenizer.decode(outputs[0])
print(response)
