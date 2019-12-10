import requests
response = requests.get("https://fortnite-api.com/shop/br?language=ru", headers={"x-api-key":"7810743c94bace6ecb065c5d1732c2fe52480d1f1a1236a0f4e34834fb4a9148"})
print(response.content)
