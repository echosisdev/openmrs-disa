from django.shortcuts import render
#from django.http import HttpResponse
from core.forms import ExcelForm
from core.models import CsvFile, ExcelFile



import csv
import pandas as pd

class LaboratoryData:
    def __init__(self, provincia, distrito, us, nome, sexo, nid, data_colheita, data_resultado, valor_carga, qualidade_carga):
        self.provincia = provincia
        self.distrito = distrito
        self.us = us
        self.nome = nome
        self.sexo = sexo
        self.nid = nid
        self.data_colheita = data_colheita
        self.data_resultado = data_resultado
        self.valor_carga = valor_carga
        self.qualidade_carga = qualidade_carga

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
        laboratory_list = []
        art = ''
        with open('uploads/laboratorio.csv', 'r') as f:
            data = csv.reader(f)
            next(data)
            for row in data:
                laboratory_list.append(
                    LaboratoryData(row[9],row[11], row[12], row[14], row[22], art, row[32], row[34], row[56], row[58])
                )
            
        for lab in laboratory_list:
           # print(f'{lab.provincia}  {lab.distrito}  {lab.us}  {lab.nome} {lab.sexo} {lab.nid} {lab.data_colheita}  {lab.data_resultado} {lab.valor_carga}  {lab.qualidade_carga}')
           pass
        print(art)
    return render(request, 'app/upload.html', {'form': form})