import re

def update_readme():
    with open('README.md', 'r') as file:
        readme_content = file.read()

    # match anything，the link should started with github
    pattern = re.compile(r'(\[.*?\]\(https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_-]+)\) - .*?)(\n|$)')
    def replacement(match):
        text, user, repo, newline = match.groups()
        if '![Forks]' in text or '![Stars]' in text:
            return match.group(0)  # skip if contains forks and stars
        return f'{text} [![Forks](https://img.shields.io/github/forks/{user}/{repo}?style=social)](https://github.com/{user}/{repo}/network/members) [![Stars](https://img.shields.io/github/stars/{user}/{repo}?style=social)](https://github.com/{user}/{repo}/stargazers){newline}'

    new_content = pattern.sub(replacement, readme_content)

    with open('README.md', 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    update_readme()
