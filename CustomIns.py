import google.generativeai as genai

# Your API key
SAI = "u r api key here "
genai.configure(api_key=SAI)

# controlling response using ins variable
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
ins = "in this chat,your name is yui and my name is sunny. Respond as if you are explainig things to fresh dumb computer science student who dont have any knowlwdge"
while(True):
    que = input("Your query : ")
    if(que.strip() == ''):
        break
    res = chat.send_message(ins+que)
    print("\n")
    print(f"Ai is saying that : {res.text}")
    print("\n")
    ins = ''




