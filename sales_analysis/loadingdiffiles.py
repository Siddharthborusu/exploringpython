import pandas as pd
# CSV
df = pd.read_csv('data/file.csv')

# JSON
df = pd.read_json('data/file.json')
# or for simple JSON:
with open('data/config.json', 'r') as f:
    data = json.load(f)

# Excel
df = pd.read_excel('data/file.xlsx')

# Text files
with open('data/file.txt', 'r') as f:
    text = f.read()