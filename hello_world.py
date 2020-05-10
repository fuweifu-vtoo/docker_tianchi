import json
import csv

# python写json
# python读csv,(逗号分隔值,Comma-Separated Values，CSV)

csv_path = '/tcdata/num_list.csv'
csv_data = []
with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    # birth_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # csv 文件按照 行row 被读取
        csv_data.append(int(row[0]))

sum_result = sum(csv_data)
csv_data.sort(reverse=True)
csv_data = csv_data[:10]

result_dict = {'Q1': 'Hello world','Q2':sum_result,'Q3':csv_data}

with open("./result.json","w") as f:
     json.dump(result_dict,f)
