from django.shortcuts import render
#from django.http import HttpResponse
from core.forms import ExcelForm
from core.models import CsvFile, ExcelFile

import csv
import pandas as pd


def upload_excel_file(request):
    form = ExcelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = ExcelForm()
        excel_file = ExcelFile.objects.get(activated=False)
        with open(excel_file.file_name.path, 'rb') as file:
            df = pd.read_excel(file, sheet_name='Resultados da Análise', skiprows=[0,1,2])
            df.to_csv(r'uploads/laboratorio.csv', index=None, header=True, encoding='utf-8')
            excel_file.activated = True
            excel_file.save()
            
       # csv_file = CsvFile.objects.get(activated=False)
        with open('uploads/laboratorio.csv', 'r') as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                print(row[59])
             
    return render(request, 'app/upload.html', {'form': form})