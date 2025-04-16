import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Utilizar un backend que no requiere interfaz gráfica
import matplotlib.pyplot as plt
import datetime
import io
import base64
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def entrenar_y_predecir(excel_file, dias_futuros=60):
    df = pd.read_excel(excel_file)
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    # Renombrar columnas
    df = df.rename(columns={
        'Ultimo': 'Close',
        'Apertura': 'Open',
        'Maximo': 'High',
        'Minimo': 'Low'
    })

    # Fecha en segundos
    df['Fecha_num'] = df['Fecha'].astype(np.int64) // 10**9

    # Tendencia de los últimos 5 días
    df['Trend'] = df['Open'].rolling(window=30).apply(lambda x: np.polyfit(range(len(x)), x, 1)[0], raw=True)
    df.dropna(inplace=True)

    X = df[['Fecha_num', 'Trend']]
    y = df['Open']

    # Split aleatorio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    modelo = RandomForestRegressor(n_estimators=100)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # Predicción futura
    fecha_actual = df['Fecha'].max()
    fecha_futura = fecha_actual + datetime.timedelta(days=dias_futuros)
    fecha_num_futura = int(fecha_futura.timestamp())

    trend_futura = df['Trend'].iloc[-1]
    X_futuro = pd.DataFrame({'Fecha_num': [fecha_num_futura], 'Trend': [trend_futura]})
    prediccion = modelo.predict(X_futuro)[0]

    # Graficar
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(df['Fecha'], df['Close'], label='Datos reales', color='blue')
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

    return image_base64, round(prediccion, 2), fecha_futura, round(mse, 2), round(rmse, 2), round(r2, 2)
