import json
import re

# 读取 JSON 数据
with open('jwfw.json', 'r', encoding='utf-8') as file:
    courses = json.load(file)

# 提取课程代码前缀
prefixes = set()
prefix_pattern = re.compile(r'^[A-Z]+[0-9]+')

for course in courses:
    match = prefix_pattern.match(course['no'])
    if match:
        prefixes.add(match.group()[:-4])

# 输出前缀
prefix_list = sorted(list(prefixes))
print("export const CODE_PREFIXES = [")
for prefix in prefix_list:
    print(f"  '{prefix}',")
print("];")
