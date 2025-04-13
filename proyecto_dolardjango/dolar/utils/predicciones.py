import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import io
import base64

def procesar_excel(excel_file):
    df = pd.read_excel(excel_file)
    df = df.rename(columns={
        'Ultimo': 'Close',
        'Apertura': 'Open',
        'Maximo': 'High',
        'Minimo': 'Low'
    })
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df.set_index('Fecha', inplace=True)
    return df

def generar_grafico_velas(df):
    buffer = io.BytesIO()
    mpf.plot(df, type='candle', style='yahoo', mav=(3, 6),
             title='Gráfico de Velas',
             savefig=dict(fname=buffer, dpi=100, format='png'))
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return image_base64
