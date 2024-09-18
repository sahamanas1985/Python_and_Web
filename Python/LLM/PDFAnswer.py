import fitz
from gpt4all import GPT4All

model_path = ".\models"
model_name = "mistral-7b-openorca.gguf2.Q4_0.gguf"  #About 4 minutes

def readpdf():
    with fitz.open("SamplePDF.pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return (text)

def readjsontemplate():
    jsonfile = open("jsonformat.json", "r")
    return (jsonfile.read())

user_prompt = "read the following text, and using the information in the text, populate the given json template."\
"\n\n" + readpdf() + " \n\n and the Json template is: \n\n " + readjsontemplate()

model = GPT4All(model_name, allow_download=False, model_path = model_path)
with model.chat_session():
    response = model.generate(prompt=user_prompt, temp=0.2, max_tokens = 1000)
    print(response)


