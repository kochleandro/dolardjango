import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Utilizar un backend que no requiere interfaz gráfica
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime
import io
import base64
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error, r2_score
import math

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

from sklearn.metrics import mean_squared_error

def entrenar_y_predecir(excel_file, dias_futuros=60):
    df = pd.read_excel(excel_file)
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    X = df[['Fecha']].apply(lambda col: col.astype(int) / 10**9)
    y = df['Apertura']

    X_train, X_test, y_train, y_test = train_test_split(X, y)
    modelo = RandomForestRegressor(n_estimators=10)
    modelo.fit(X_train, y_train)

    # Evaluación del modelo
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rmse = math.sqrt(mse)  # Calcula la raíz cuadrada del MSE

    # Predicción futura
    fecha_actual = df['Fecha'].max()
    fecha_futura = fecha_actual + datetime.timedelta(days=dias_futuros)
    X_futuro = pd.DataFrame({'Fecha': [fecha_futura]}).apply(lambda col: col.astype(int) / 10**9)
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

    return image_base64, round(prediccion, 2), fecha_futura, round(mse, 2), round(rmse, 2), round(r2, 2)