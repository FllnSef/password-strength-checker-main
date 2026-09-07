import secrets
import string

def generate_password(length=10):
    # Определение наборов символов
    lowercase = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    uppercase = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits             # 0123456789
    special = string.punctuation       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # 1. Гарантируем, что в пароле будет МИНИМУМ по одному символу каждого типа
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # 2. Объединяем все символы для заполнения остатка пароля
    all_characters = lowercase + uppercase + digits + special

    # 3. Добираем оставшиеся 6 символов из случайной смеси всех наборов
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # 4. Перемешиваем символы, чтобы категории не шли всегда в одном порядке
    secrets.SystemRandom().shuffle(password)

    # 5. Преобразуем список в готовую строку
    return "".join(password)

# --- Пример использования ---
if __name__ == "__main__":
    print("=" * 40)
    print("    ГЕНЕРАТОР НАДЕЖНЫХ ПАРОЛЕЙ (10 символов)")
    print("=" * 40)

    # Сгенерируем 5 вариантов паролей
    print("\nСгенерированные пароли:")
    for i in range(1, 6):
        new_password = generate_password(10)
        print(f"Вариант {i}:  {new_password}")