import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import torch
import os
import torch.optim as optim
import torch.nn as nn
import matplotlib.pyplot as plt

path = os.path.abspath(os.path.join(os.path.dirname(__file__),"training_data.csv"))

df = pd.read_csv(path)

df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values(by='Date')

df.set_index('Date', inplace=True)

scaler = MinMaxScaler()
df['Pinar del Rio'] = scaler.fit_transform(df[['Pinar del Rio']])

def create_sequences(data, timesteps):
    X, y = [], []
    for i in range(len(data) - timesteps):
        X.append(data[i:i+timesteps])
        y.append(data[i+timesteps])
    return np.array(X), np.array(y)

timesteps = 7  # Tamaño de las secuencias, cuántos días hacia atrás se usarán para predecir el siguiente
# esto es un hiperparámetro que se puede ajustar, creo que tiene problemas por los datos no periodicos


X, y = create_sequences(df['Pinar del Rio'].values, timesteps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(-1)  
X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(-1)
y_train = torch.tensor(y_train, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

print("Cantidad de datos a entrenar")
print(X_train.shape)

print("Cantidad de datos a testear")
print(X_test.shape)

class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  
        return out

# Crear el modelo
input_size = 1
hidden_size = 16
output_size = 1
model = SimpleRNN(input_size, hidden_size, output_size)


# Definir la pérdida y el optimizador
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Entrenamiento
epochs = 200
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    
    # Predicciones y cálculo de la pérdida
    outputs = model(X_train)
    loss = criterion(outputs.squeeze(), y_train)
    
    # Retropropagación
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 20 == 0:
        print(f"Época {epoch + 1}/{epochs}, Pérdida: {loss.item():.4f}")


model.eval()
with torch.no_grad():
    y_pred = model(X_test).squeeze()
    test_loss = criterion(y_pred, y_test)
    print(f"Pérdida en el conjunto de prueba: {test_loss.item():.4f}")

# Desnormalizar los valores predichos y reales
y_test_inv = scaler.inverse_transform(y_test.numpy().reshape(-1, 1))
y_pred_inv = scaler.inverse_transform(y_pred.numpy().reshape(-1, 1))


# una prediccion random para comparar tambien en la tabla
randomprediction = []

for i in range(len(y_test_inv)):
    randomprediction.append(np.random.uniform(0,300))

randomprediction = np.array(randomprediction)



# Graficar resultados
plt.figure(figsize=(10, 6))
print(y_test_inv)
plt.plot(y_test_inv, label="Real", marker='o')
plt.plot(y_pred_inv, label="Predicción", marker='x')
plt.plot(randomprediction, label="Random", marker='x')
plt.legend()
plt.title("Predicción vs Real")
plt.show()


# Tomar la última secuencia del conjunto completo para predecir
last_sequence = torch.tensor(df['Pinar del Rio'].values[-timesteps:], dtype=torch.float32).unsqueeze(0).unsqueeze(-1)

# Predicción
model.eval()
with torch.no_grad():
    next_value = model(last_sequence).item()

# Desnormalizar el valor predicho
next_value_inv = scaler.inverse_transform([[next_value]])
print("Predicción para el siguiente día:", next_value_inv[0][0])

# error cuadratico medio

mse = mean_squared_error(y_test_inv, y_pred_inv)
print("Error cuadrático medio:", mse)
