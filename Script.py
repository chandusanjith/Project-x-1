import csv

csv_path = '/Users/chandusanjith/Desktop/automation_script.csv'
description = 'Description'
product_owner = 'Product Owner'


out_list = []
out_dict = {}

with open(csv_path,'rt')as f:
  data = csv.reader(f)
  next(data, None)
  for row in data:
        out_dict['businessUnit'] = row[0]
        out_dict['auth'] = 'JWT'
        out_dict['serviceUrls'] = []
        out_dict['serviceUrls'].append('https://data.fmrco.com')
        out_dict['name'] = row[3]
        out_dict['description'] = description
        out_dict['applicationId'] = row[1]
        out_dict['productOwner'] = product_owner
        out_dict['dataSources'] = []
        out_dict['dataSources'].append({})
        out_dict['dataSources'][0]['source'] = 'DX'
        out_dict['dataSources'][0]['url'] = row[2]
        out_dict['apiType'] = {}
        out_dict['apiType']['type'] = row[4]
        out_dict['apiType']['openApiSpecification'] = ''
        out_list.append(out_dict)
for payload in out_list:
    print(payload)
