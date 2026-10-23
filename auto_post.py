import json, os, requests

TOKEN = os.environ["LINKEDIN_ACCESS_TOKEN"]
AUTHOR_URN = os.environ["LINKEDIN_PERSON_URN"] # e.g., "urn:li:person:YOUR_ID"

with open("posts_queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

next_post = next((item for item in queue if not item["posted"]), None)
if not next_post:
    print("All queued posts are already published!")
    exit(0)

url = "https://api.linkedin.com/v2/ugcPosts"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

payload = {
    "author": AUTHOR_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": next_post["content"]},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

res = requests.post(url, headers=headers, json=payload)
res.raise_for_status()

next_post["posted"] = True
with open("posts_queue.json", "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully published Day {next_post['day']}!")