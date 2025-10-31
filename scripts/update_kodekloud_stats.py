import os
import requests
import re
import json

email = os.environ["KK_EMAIL"]
password = os.environ["KK_PASSWORD"]

# Start session
session = requests.Session()

# Login and get JWT token
auth = session.post(
    "https://engineer.kodekloud.com/auth/local",
    json={"identifier": email, "password": password},
)



if auth.status_code != 200:
    print("❌ Login failed. Please verify KK_EMAIL and KK_PASSWORD secrets.")
    print(auth.text)
    exit(1)

jwt = auth.json().get("jwt")
headers = {"Authorization": f"Bearer {jwt}"}

# Get leaderboard data (DevOps Architect tier)
r = session.get(
    "https://engineer.kodekloud.com/api/leaderboards/devops-architect",
    headers=headers,
)
if r.status_code != 200:
    print("❌ Failed to fetch leaderboard data.")
    print(r.text)
    exit(1)

data = r.json()

your_name = "Charles Vosloo"
rank = None
points = None

for entry in data:
    if your_name.lower() in entry["user"]["username"].lower():
        rank = entry["rank"]
        points = entry["points"]
        break

if not rank:
    print("❌ Could not find your username in the leaderboard data.")
    exit(1)

# Update README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- KK_STATS_START -->"
end = "<!-- KK_STATS_END -->"
replacement = f"""{start}
**Current Rank:** #{rank}  
**Total Points:** {points}
{end}"""

readme = re.sub(f"{start}.*?{end}", replacement, readme, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print(f"✅ Updated README with rank #{rank} and {points} points.")

