from openai import OpenAI
client = OpenAI(api_key=st.secrets["API_KEY"])
prompt = "Hello, how are you?"

completion = client.chat.completions.create(
  model="gpt-5.2",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
