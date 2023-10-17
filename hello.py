
import requests
import pandas as pd

import os

url = 'https://app.nanonets.com/api/v2/OCR/Model/1163b36b-f301-4c17-9190-bdaf0bb6fdbc/LabelUrls/?async=false'

headers = {
    'accept': 'application/x-www-form-urlencoded'
}

def tableJson(filename):
  data = {'file': open('./images/'+filename, 'rb')}
  # response = requests.request('POST', url, headers=headers, auth=requests.auth.HTTPBasicAuth('966ce9be-a36c-11ed-bfd4-0aa2bf907cfe', ''), data=data)
  response = requests.post(url, auth=requests.auth.HTTPBasicAuth('966ce9be-a36c-11ed-bfd4-0aa2bf907cfe', ''), files=data)
  res =  response.json()
  data = res.get('result')
  # data =  [{'message': 'Success', 'input': 'img.png', 'prediction': [{'id': '60523206-2f74-4f6e-87e7-cea5d6181766', 'label': 'table', 'xmin': 261, 'ymin': 131, 'xmax': 824, 'ymax': 278, 'score': 1, 'ocr_text': 'table', 'type': 'table', 'cells': [{'id': '972ece4c-1cad-4a40-aa3f-48e6e020467c', 'row': 1, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 261, 'ymin': 131, 'xmax': 513, 'ymax': 169, 'score': 0.9326172, 'text': 'Nancy Bowland', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'b291c0d1-e053-4bc1-bb74-4b37ea53a263', 'row': 1, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 513, 'ymin': 131, 'xmax': 824, 'ymax': 169, 'score': 0.94189453, 'text': 'Sharonda McMurray', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'c535bcb3-529c-48d4-b536-4b9a3345000e', 'row': 2, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 261, 'ymin': 169, 'xmax': 513, 'ymax': 206, 'score': 0.8413086, 'text': 'Gary Hicks', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '9cb4c764-1430-411e-9cc3-210a42eba4ee', 'row': 2, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 513, 'ymin': 169, 'xmax': 824, 'ymax': 206, 'score': 0.8491211, 'text': 'Nancy Montgomery', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'cd157390-f657-499b-8f0e-f482130af8b1', 'row': 3, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 261, 'ymin': 206, 'xmax': 513, 'ymax': 242, 'score': 0.7084961, 'text': 'Todd Holbrook', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '42fd6e71-eeda-4c53-a340-4743ea4f14dc', 'row': 3, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 513, 'ymin': 206, 'xmax': 824, 'ymax': 242, 'score': 0.71533203, 'text': "Brice O'Brien", 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'c2fab66d-269c-4645-a713-bb16c1871c88', 'row': 4, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 261, 'ymin': 242, 'xmax': 513, 'ymax': 278, 'score': 0.7680664, 'text': 'Cindi Hunter', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '2eb30d64-41e7-433b-a805-ece4b6cb6be1', 'row': 4, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 513, 'ymin': 242, 'xmax': 824, 'ymax': 278, 'score': 0.7753906, 'text': 'Donna Walkup', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}], 'status': 'correctly_predicted', 'page_no': 0, 'label_id': ''}, {'id': 'e0904c14-e557-4e57-867b-d692325c4299', 'label': 'table', 'xmin': 162, 'ymin': 650, 'xmax': 1302, 'ymax': 969, 'score': 1, 'ocr_text': 'table', 'type': 'table', 'cells': [{'id': '58b44afb-8b36-4361-821c-5c11faf75ffd', 'row': 1, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 650, 'xmax': 1204, 'ymax': 687, 'score': 0.8383789, 'text': 'Reasons for Consumer Contact :', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '01b1c7a4-ffec-4850-b33c-45a1973ff737', 'row': 1, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 650, 'xmax': 1302, 'ymax': 687, 'score': 0.7871094, 'text': '%', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '5fd5728b-16ef-410c-85da-5a70a72d55d2', 'row': 2, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 687, 'xmax': 1204, 'ymax': 722, 'score': 0.91503906, 'text': 'Request Catalog / Order Form', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '70ced10e-a7dc-471e-90da-547b75e18065', 'row': 2, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 687, 'xmax': 1302, 'ymax': 722, 'score': 0.8588867, 'text': '55 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '6bcd3c66-a93a-4b92-84f0-0da5205fe03e', 'row': 3, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 722, 'xmax': 1204, 'ymax': 757, 'score': 0.8989258, 'text': 'Order Status', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '478b208d-1550-4148-b5c3-c6c6f0c9601e', 'row': 3, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 722, 'xmax': 1302, 'ymax': 757, 'score': 0.84375, 'text': '19 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '0adca338-bdff-471c-a82f-1ffe24a07017', 'row': 4, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 757, 'xmax': 1204, 'ymax': 793, 'score': 0.8935547, 'text': 'Mailing List Request ( add , change , update add , target change )', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '02389143-659f-4827-924e-baf6ed3b8e0b', 'row': 4, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 757, 'xmax': 1302, 'ymax': 793, 'score': 0.8388672, 'text': '14 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'a7350a9f-09a4-4a21-bb73-2983e726e00f', 'row': 5, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 793, 'xmax': 1204, 'ymax': 827, 'score': 0.84375, 'text': 'Promotional Questions ( lists , seals / c - notes questions , terms , Web issues , etc. )', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'dcd667e1-1bb2-4b30-adff-f75a8997ee52', 'row': 5, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 793, 'xmax': 1302, 'ymax': 827, 'score': 0.79248047, 'text': '5 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '68988cfb-ab14-4fb4-b903-b3a223cd2c70', 'row': 6, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 827, 'xmax': 1204, 'ymax': 863, 'score': 0.8935547, 'text': 'Product Issues', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'e75e8207-5c94-4e32-87ca-5816a691b704', 'row': 6, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 827, 'xmax': 1302, 'ymax': 864, 'score': 0.8388672, 'text': '4 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'cfab72b9-e0ec-4847-a8ac-20ed53bce867', 'row': 7, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 863, 'xmax': 1204, 'ymax': 898, 'score': 0.8979492, 'text': 'Non - receipt DM , conversion , fulfillment', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'b8475c98-2a7e-4342-aead-8231ce3a4d2b', 'row': 7, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 863, 'xmax': 1302, 'ymax': 898, 'score': 0.8432617, 'text': '1 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '0bce9e14-2ef1-4df3-8ac3-6cf48c563b1e', 'row': 8, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 897, 'xmax': 1204, 'ymax': 934, 'score': 0.89501953, 'text': 'ELP Issues card request , statement issues', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '0f5d6785-b903-4542-bfa1-de54ea6d6411', 'row': 8, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 898, 'xmax': 1302, 'ymax': 934, 'score': 0.84033203, 'text': '1 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': 'd2048446-ddf8-43d3-8059-75276af529d7', 'row': 9, 'col': 1, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 162, 'ymin': 933, 'xmax': 1204, 'ymax': 969, 'score': 0.9355469, 'text': 'Other', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}, {'id': '30cb42dc-c821-4c01-955d-47877e4d3953', 'row': 9, 'col': 2, 'row_span': 1, 'col_span': 1, 'label': '', 'xmin': 1204, 'ymin': 934, 'xmax': 1302, 'ymax': 969, 'score': 0.87841797, 'text': '1 %', 'row_label': '', 'verification_status': 'correctly_predicted', 'status': '', 'failed_validation': '', 'label_id': ''}], 'status': 'correctly_predicted', 'page_no': 0, 'label_id': ''}], 'page': 0, 'request_file_id': '4a34be14-049d-4218-905a-bc7f1c7de35e', 'filepath': 'uploadedfiles/1163b36b-f301-4c17-9190-bdaf0bb6fdbc/PredictionImages/ecdad5dd-411c-46cf-a26d-a738f9b61c85.jpeg', 'id': '1ee87a1b-6cb7-11ee-8b91-7eb9c20dd504', 'rotation': 0, 'file_url': 'uploadedfiles/1163b36b-f301-4c17-9190-bdaf0bb6fdbc/RawPredictions/4a34be14-049d-4218-905a-bc7f1c7de35e.png', 'request_metadata': '', 'processing_type': 'sync', 'size': {'width': 1343, 'height': 986}}]

  table = []

  for i in data[0].get('prediction'):
    cells = []
    for j in i.get('cells'):
          custom = {}
          custom['row'] = j.get('row')
          custom['col'] = j.get('col')
          custom['text'] = j.get('text')
          cells.append(custom)
    table.append(cells)
    
  result_table = []
  for i in table:
    row = []
    row_max = 0
    col_max = 0
    for j in i:
      row_max = max(row_max, j.get('row'))
      col_max = max(col_max, j.get('col'))
    for x in range(row_max):
      col = []
      for y in range(col_max):
        col.append(i[x*col_max+y].get('text'))
      row.append(col)
    result_table.append(row)
    
      
    # result_table.append(df.to_json(orient='records'))
  payload = {
    "table_count": len(data[0].get('prediction')),
    "tables": result_table
  }
  return payload


print(tableJson('img.png'))