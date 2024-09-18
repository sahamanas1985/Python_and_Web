from gpt4all import GPT4All

model_path = ".\models"
model_name = "mistral-7b-openorca.gguf2.Q4_0.gguf"

user_prompt = "an sql table named tbl_users has the following columns and data types \
userid (int), username (nvarchar), age (int), birthday (datetime), gender (nvarchar) \
another sql table named tbl_salary has the following columns and data types \
userid (int), salary (decimal) \
write an sql query that can show username, age, and salary for all female users \
who were born between 1980 and 2000 \
just write the sql without any additional text or explanation."


model = GPT4All(model_name, allow_download=False, model_path = model_path)
with model.chat_session():
    response = model.generate(prompt=user_prompt, temp=0.2)
    print(response)