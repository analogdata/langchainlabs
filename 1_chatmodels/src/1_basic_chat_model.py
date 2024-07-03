import os
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))

result = model.invoke("What is 81 divided by 9 ?")

print("Result: ")
print(result)

print("Content: ")
print(result.content)