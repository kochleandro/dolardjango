import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime
import io
import base64
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

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

def entrenar_y_predecir(excel_file, dias_futuros=180):
    df = pd.read_excel(excel_file)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    X = df[['Fecha']].apply(lambda col: col.astype(int) / 10**9)  # convertir fechas a timestamp
    y = df['Apertura']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    modelo = RandomForestRegressor(n_estimators=10)
    modelo.fit(X_train, y_train)

    fecha_actual = df['Fecha'].max()
    fecha_futura = fecha_actual + datetime.timedelta(days=dias_futuros)
    X_futuro = pd.DataFrame({'Fecha': [fecha_futura]})
    X_futuro = X_futuro.apply(lambda col: col.astype(int) / 10**9)

    prediccion = modelo.predict(X_futuro)[0]

    # Graficar
    fig, ax = plt.subplots(figsize=(10,5))
    plt.plot(df['Fecha'], df['Ultimo'], label='Datos reales', color='blue')
    plt.plot(fecha_futura, prediccion, marker='o', color='red', label='Predicción')
    plt.xlabel('Fecha')
    plt.ylabel('Cotización')
    plt.title('Predicción de Cotización')
    plt.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return image_base64, prediccion, fecha_futura


def generar_grafico_velas(df):
    buffer = io.BytesIO()
    mpf.plot(df, type='candle', style='yahoo', mav=(3, 6),
             title='Gráfico de Velas',
             savefig=dict(fname=buffer, dpi=100, format='png'))
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return image_base64
