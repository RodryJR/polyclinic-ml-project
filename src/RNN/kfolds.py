from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, accuracy_score, r2_score
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


timesteps = 7  

X, y = create_sequences(df['Pinar del Rio'].values, timesteps)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(-1)  
X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(-1)
y_train = torch.tensor(y_train, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

input_size = 1
hidden_size = 16
output_size = 1

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

# Número de folds
k_folds = 5

kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)

fold_metrics = []

# validación cruzada
for fold, (train_idx, test_idx) in enumerate(kf.split(X, y)):
    print(f"Fold {fold + 1}/{k_folds}")
    
    X_train_fold, X_test_fold = X[train_idx], X[test_idx]
    y_train_fold, y_test_fold = y[train_idx], y[test_idx]

    X_train_fold = torch.tensor(X_train_fold, dtype=torch.float32).unsqueeze(-1)
    X_test_fold = torch.tensor(X_test_fold, dtype=torch.float32).unsqueeze(-1)
    y_train_fold = torch.tensor(y_train_fold, dtype=torch.float32)
    y_test_fold = torch.tensor(y_test_fold, dtype=torch.float32)

    # Inicializar un nuevo modelo para este fold
    model = SimpleRNN(input_size, hidden_size, output_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    epochs = 100  
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(X_train_fold)
        loss = criterion(outputs.squeeze(), y_train_fold)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        y_pred_fold = model(X_test_fold).squeeze()
        fold_rmse = np.sqrt(mean_squared_error(scaler.inverse_transform(y_test_fold.numpy().reshape(-1, 1)), scaler.inverse_transform(y_pred_fold.numpy().reshape(-1, 1))))
        fold_r2 = r2_score(y_test_fold.numpy(), y_pred_fold.numpy())

    # Almacenar métricas del fold
    fold_metrics.append({"fold": fold + 1, "rmse": fold_rmse, "r2": fold_r2})
    print(f"Fold {fold + 1}: RMSE={fold_rmse:.4f}, R2={fold_r2:.4f}")


# Calcular métricas promedio
avg_rmse = np.mean([m["rmse"] for m in fold_metrics])
avg_r2 = np.mean([m["r2"] for m in fold_metrics])
print("\nResultados de Validación Cruzada:")
print(f"RMSE Promedio: {avg_rmse:.4f}")
print(f"R2 Promedio: {avg_r2:.4f}")
