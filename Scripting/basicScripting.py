def clean_text(t):
    return t.lower().strip()

texts = ["Hello", "WORLD"]
result = [clean_text(x) for x in texts]

print(result)
