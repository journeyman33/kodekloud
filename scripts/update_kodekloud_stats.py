import os

readme_path = "README.md"

def update_readme():
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start = "<!-- KK_STATS_START -->"
    end = "<!-- KK_STATS_END -->"
    before = content.split(start)[0]
    after = content.split(end)[1]

    stats = """
**Current Rank:** #5  
**Total Points:** 363,955  
_Last updated manually (API not yet available)_
    """

    updated = f"{before}{start}\n{stats}\n{end}{after}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    print("✅ Skipping KodeKloud login (protected by Cloudflare)")
    update_readme()

