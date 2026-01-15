# Test Task — Email Domains & Telegram Integration

## 1. Email Domain Check

Python-скрипт проверяет список email-адресов:
- существование домена
- наличие MX-записей

Для каждого email выводится статус:
- «домен валиден»
- «домен отсутствует»
- «MX-записи отсутствуют или некорректны»

### Запуск

1. Установить Python 3.10+
2. Установить зависимости:
   python -m pip install dnspython
3. Запустить:
   python check_email_domains.py

---

## 2. Telegram Integration

Реализован Python-скрипт, который:
- читает текст из файла `message.txt`
- отправляет его в приватный Telegram-чат через Telegram-бота
<img width="653" height="769" alt="image" src="https://github.com/user-attachments/assets/1a3855e9-331e-4410-a584-83bada5919ac" />


### Подготовка

1. Создать Telegram-бота через @BotFather
2. Получить BOT TOKEN
3. Узнать `chat_id` через метод `getUpdates`
4. Указать значения в файле `send_to_telegram.py`:

   TOKEN = "TELEGRAM_BOT_TOKEN"  
   CHAT_ID = <chat_id>

### Запуск

1. Установить зависимости:
   python -m pip install requests
2. Запустить:
   python send_to_telegram.py

Сообщение из `message.txt` будет отправлено в указанный Telegram-чат.

---

## Структура проекта

- check_email_domains.py — проверка email-доменов и MX-записей
- send_to_telegram.py — отправка текста в Telegram
- message.txt — текст сообщения
- architecture.md — описание архитектурного решения


# email-test-task
email_domain_telegram_test
