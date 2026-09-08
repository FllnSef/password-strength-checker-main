import secrets
import string

def generate_password(length=10):
   
    lowercase = string.ascii_lowercase  
    uppercase = string.ascii_uppercase  
    digits = string.digits             
    special = string.punctuation       

    
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

   
    all_characters = lowercase + uppercase + digits + special

    
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    
    secrets.SystemRandom().shuffle(password)

    
    return "".join(password)


if __name__ == "__main__":
    print("=" * 40)
    print("    ГЕНЕРАТОР НАДЕЖНЫХ ПАРОЛЕЙ (10 символов)")
    print("=" * 40)

    # Сгенерируем 5 вариантов паролей
    print("\nСгенерированные пароли:")
    for i in range(1, 6):
        new_password = generate_password(10)
        print(f"Вариант {i}:  {new_password}")