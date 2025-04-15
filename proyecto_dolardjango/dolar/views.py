from django.shortcuts import render
from .utils.predicciones import entrenar_y_predecir

def subir_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['archivo']
        dias = int(request.POST.get('dias', 60))  # Tomar los días del formulario
        grafico, prediccion, fecha = entrenar_y_predecir(excel_file, dias_futuros=dias)
        return render(request, 'resultado.html', {
            'grafico': grafico,
            'prediccion': round(prediccion, 2),
            'fecha': fecha.strftime('%Y-%m-%d'),
            'dias': dias
        })
    return render(request, 'subir_excel.html')

