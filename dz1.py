import numpy as np
import matplotlib.pyplot as plt

# Параметры сигнала
fs = 1e6  # Частота дискретизации (1 МГц)
t = np.arange(0, 1e-3, 1/fs)  # Время (1 мс)

# Генерация треугольного сигнала
def triangle_wave(t, period, amplitude):
    return amplitude * (2 * (t % period) / period - 1)

f1, f2, f3 = 10e3, 5e3, 2e3  # Частоты (10 кГц, 5 кГц, 2 кГц)
A = 5  # Амплитуда

signal = triangle_wave(t, 1/f1, A) + triangle_wave(t, 1/f2, A) + triangle_wave(t, 1/f3, A)

# Визуализация исходного сигнала
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t*1e3, signal, label='Исходный сигнал')
plt.legend()

# Запрещенная зона
forbidden_zone = (2, 4)

# Применение логического каскада
digital_signal = np.where(signal > forbidden_zone[1], 5, np.where(signal < forbidden_zone[0], 0, signal))

# Визуализация цифрового сигнала
plt.subplot(3, 1, 2)
plt.plot(t*1e3, digital_signal, label='Цифровой сигнал')
plt.legend()

# Визуализация запрещенной зоны
plt.subplot(3, 1, 3)
plt.plot(t*1e3, signal, label='Исходный сигнал')
plt.axhline(forbidden_zone[0], color='r', linestyle='--', label='Нижняя граница')
plt.axhline(forbidden_zone[1], color='g', linestyle='--', label='Верхняя граница')
plt.legend()

plt.tight_layout()
plt.show()
