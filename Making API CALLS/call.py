import requests

response = requests.post("https://api.openai.com/v1/chat/completions",
                         headers={"Authorization": f"Bearer YOUR_KEY"},
                         json={
                             "model": "gpt-4o",
                             "messages":[{"role":"user","content":"Who is Ronlado"}]
                         })
print(response.json())