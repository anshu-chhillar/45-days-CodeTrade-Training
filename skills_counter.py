#skills_counter.py has a list of skills and prints a numbered list of skills and their total count


skills = [
    "Python",
    "SQL",
    "Git",
    "Machine Learning",
    "JavaScript"
]

for index,skill in enumerate(skills,start=1):
    print(f"{index}.{skill}")

print(f"\nTotal skills: {len(skills)}")