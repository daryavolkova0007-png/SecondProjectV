"""
Демонстрация системы уведомлений GitHub
"""

def send_notification(user, message_type, content):
    """
    Симуляция системы уведомлений GitHub
    """
    notifications = {
        "pull_request": "🔔 Новый Pull Request от {}",
        "issue": "📋 Новая Issue назначена на {}",
        "mention": "👤 Вас упомянули в комментарии {}",
        "reminder": "⏰ Напоминание: {}"
    }
    
    template = notifications.get(message_type, "📢 Уведомление: {}")
    return template.format(content)

# Тестирование уведомлений
if __name__ == "__main__":
    print("Тест системы уведомлений:")
    print(send_notification("@daryavolkova0007-png", "pull_request", "добавлена новая функциональность"))
    print(send_notification("@kamila-zakiriayeva", "mention", "проверьте код"))
    print(send_notification("team", "reminder", "еженедельный обзор проекта"))
