"""есть:"""
words = [
    "python",
    "sql",
    "python",
    "docker",
    "sql",
    "python",
    "git"
]
"""
Нужно получить:
{
    "python": 3,
    "sql": 2,
    "docker": 1,
    "git": 1
}
"""
answer={}
for word in words:
    if word in answer:
        answer[word] += 1
    else:
        answer[word] = 1
print(answer)