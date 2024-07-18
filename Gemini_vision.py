# install google.generativeai pkg
# next just copy paste my code in your ide
import google.generativeai as genai
from pathlib import Path
genai.configure(api_key="U r api here ")
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 8192,
    # "response_mime_type": "text/plain",

}
# history = []
model = genai.GenerativeModel("gemini-pro-vision", generation_config=generation_config)
inp  = input("enter img path")
sai = input("enter what u wanna ask about that png file")

img_path = Path(inp)
img_part = {
    "mime_type": "image/png",
    "data": img_path.read_bytes(),
}
prom = [
    f"{sai}:\n",img_part
]

res = model.generate_content(prom)

# print(res.text)
for chunk in res:
    print(chunk.text, end="", flush=True)
