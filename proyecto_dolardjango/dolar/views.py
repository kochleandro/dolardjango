from django.shortcuts import render
from .utils.predicciones import entrenar_y_predecir
from django.contrib import messages
from django.shortcuts import render, redirect


def subir_excel(request):
    if request.method == 'POST':
        if 'archivo' not in request.FILES or not request.FILES['archivo']:
            messages.error(request, "Debes seleccionar un archivo antes de continuar.")
            return redirect('subir_excel')

        try:
            excel_file = request.FILES['archivo']
            dias = int(request.POST.get('dias', 60))
            grafico, prediccion, fecha, mse, rmse, r2 = entrenar_y_predecir(excel_file, dias_futuros=dias)
            return render(request, 'resultado.html', {
                'grafico': grafico,
                'prediccion': prediccion,
                'fecha': fecha.strftime('%Y-%m-%d'),
                'dias': dias,
                'mse': mse,
                'rmse': rmse,  # Incluye rmse en el contexto
                'r2': r2
            })
        except Exception as e:
            # Manejo de errores en caso de que falle la predicción
            messages.error(request, f"Ocurrió un error: {str(e)}")
            return redirect('subir_excel')
            
    return render(request, 'subir_excel.html')




