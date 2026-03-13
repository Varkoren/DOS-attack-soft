<p align="center">
  <img src="https://img.shields.io/badge/Version-6.4-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

<h1 align="center">🌪️ VARKOREN STORM v6.4</h1>

<p align="center">
  <strong>Мощная гибридная утилита для стресс-тестирования сетевой инфраструктуры</strong>
</p>

---

### 📌 Описание проекта
**VARKOREN STORM** - это профессиональный инструмент для анализа устойчивости серверов к критическим нагрузкам. Скрипт использует низкоуровневое управление сокетами для создания комбинированного трафика (TCP + UDP), что позволяет выявить слабые места как в пропускной способности канала, так и в логике обработки соединений.

### 🚀 Ключевые особенности
* **Hybrid Flood** - одновременная атака по протоколам TCP и UDP.
* **Heavy Payload** - пакеты весом до 16 КБ для имитации реальной нагрузки.
* **Live Monitor** - интерактивный дашборд с отображением RPS и статуса цели.
* **Smart Bypass** - оптимизированные задержки для предотвращения блокировки со стороны локальной ОС.

---

### 🛠️ Инструкция по установке

1.  **Клонирование репозитория:**
    ```bash
    git clone [https://github.com/Varkoren/DOS-attack-soft.git](https://github.com/Varkoren/DOS-attack-soft.git)
    ```

2.  **Переход в директорию:**
    ```bash
    cd DOS-attack-soft
    ```

3.  **Установка необходимых модулей:**
    ```bash
    pip install -r requirements.txt
    ```

---

### ⚡ Быстрый запуск и режимы

Для запуска введите в терминале:
```bash
python main.py
```
| Режим | Потоки | Вес пакета | Описание |
| :--- | :--- | :--- | :--- |
| **LOW** | 300 | 1 КБ | Базовая проверка лимитов. |
| **MEDIUM** | 800 | 4 КБ | Стабильная нагрузка (лаг). |
| **OVERLOAD** | 1500 | 8 КБ | Критическая нагрузка (Stress). |
| **ULTIMATE** | 2500 | 16 КБ | Максимальный штурм (Meltdown). |
## ⚠️ Disclaimer

> [!CAUTION]
> **Project for Educational Purposes Only**
>
> 1. Автор (**VARKOREN**) не несет ответственности за неправомерное использование софта.
> 2. Программа создана для проведения стресс-тестов собственных систем.
> 3. Любые действия, нарушающие закон, остаются на совести пользователя.

---
<p align="center">
  <b>Developed by VARKOREN</b>
</p>
