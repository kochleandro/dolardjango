from django.shortcuts import render
from .utils.predicciones import entrenar_y_predecir
from django.contrib import messages


def subir_excel(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES['archivo']
            dias = int(request.POST.get('dias', 60))
            grafico, prediccion, fecha, mse, r2 = entrenar_y_predecir(excel_file, dias_futuros=dias)
            return render(request, 'resultado.html', {
                'grafico': grafico,
                'prediccion': prediccion,
                'fecha': fecha.strftime('%Y-%m-%d'),
                'dias': dias,
                'mse': mse,
                'r2': r2
            })
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {str(e)}")
            return redirect('subir_excel')  # o renderizar la misma plantilla con error
    return render(request, 'subir_excel.html')




