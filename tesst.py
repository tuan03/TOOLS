import csv

# Dữ liệu ban đầu để ghi đè vào file
data = [
    ['user2@example.com', 'password2']
]

# Ghi đè (overwrite) vào file CSV
with open('data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Đã ghi đè vào file data.csv")
