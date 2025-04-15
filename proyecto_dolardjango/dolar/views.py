from django.shortcuts import render
from .utils.predicciones import procesar_excel, generar_grafico_velas

def subir_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['archivo']
        df = procesar_excel(excel_file)
        grafico_base64 = generar_grafico_velas(df)
        return render(request, 'resultado.html', {'grafico': grafico_base64})
    return render(request, 'subir_excel.html')

