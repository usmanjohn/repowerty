import json
file_path = 'practice_only.json'
ADMIN_ID = 11
with open(file_path, "r", encoding = "utf-8") as f:
    data = json.load(f)

for obj in data:
    if obj["model"] == "gmat.pracitcequestions":
        obj["fields"]["made_by"]=ADMIN_ID
with open(file_path, "w", encoding = "utf-8") as f:
    json.dump(data, f, indent =2, ensure_ascii = False)
print('amazing!', ADMIN_ID)