import requests
import smtplib
from discord import Webhook, RequestsWebhookAdapter

# Configuration for alerts
DISCORD_WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_TELEGRAM_CHAT_ID'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

def send_discord_alert(message):
    webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
    webhook.send(message)

def send_telegram_alert(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=data)

def send_email_alert(subject, message):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = f'Subject: {subject}\n\n{message}'
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

# Example usage for large bets detected
large_bet_amount = 10000  # This could be a dynamic value
if large_bet_amount > 5000:
    alert_message = f'Large bet detected: ${large_bet_amount}'
    send_discord_alert(alert_message)
    send_telegram_alert(alert_message)
    send_email_alert('Large Bet Alert', alert_message)