import sys
import openai
import config
import random

openai.api_key = config.OPENAI_API_KEY
temperature = round(random.uniform(1, 10)/10, 1)
print(temperature)

response = openai.Completion.create(
    engine="text-davinci-003",               # select model
    prompt=sys.argv[1],
    max_tokens=1024,                         # response tokens
    temperature=temperature,                 # diversity related
    top_p=0.75,                              # diversity related
    n=1,                                     # num of response
)

completed_text = response["choices"][0]["text"]
print(completed_text)
