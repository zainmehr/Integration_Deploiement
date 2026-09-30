import os

a = 2
print("coucou", a)

token = os.environ.get("SECRET_API_TOKEN")

if token is None:
    print("❌ Le secret n'est pas défini")
else:
    print("✅ Secret récupéré, longueur :", len(token))
    print("Le token vaut 42 ?", token == "42")