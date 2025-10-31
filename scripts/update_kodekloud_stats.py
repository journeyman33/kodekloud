import os
import requests
from bs4 import BeautifulSoup
import re

email = os.environ["KK_EMAIL"]
password = os.environ["KK_PASSWORD"]

session = requests.Session()

# Login endpoint (standard credentials login)
login_response = session.post("https://engineer.kodekloud.com/auth/local", json={
    "identifier": email,
    "password": password
})

if login_response.status_code != 200:
    print("❌ Login failed! Check credentials in GitHub Secrets.")
    exit(1)

# Get leaderboard page
page = session.get("https://engineer.kodekloud.com/leaderboard")
soup = BeautifulSoup(page.text, "html.parser")

your_name = "Charles Vosloo"

user_row = soup.find("div", string=lambda x: x and your_name in x)
if not user_row:
    print("❌ Could not locate your name in leaderboard. Check spelling in script.")
    exit(1)

rank = user_row.find_previous("div").text.strip()
points = user_row.find_next("div").text.strip()

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

print("✅ README updated with latest KodeKloud stats!")
