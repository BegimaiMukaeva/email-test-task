import dns.resolver

emails = [
    "test@gmail.com",
    "hello@nonexistentdomain12345.com",
    "info@example.com"
]

def check_domain(email):
    try:
        domain = email.split("@")[1]
    except IndexError:
        return "некорректный email"

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        if answers:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
    except dns.resolver.NXDOMAIN:
        return "домен отсутствует"
    except dns.resolver.NoAnswer:
        return "MX-записи отсутствуют или некорректны"
    except Exception:
        return "ошибка при проверке"

for email in emails:
    status = check_domain(email)
    print(f"{email}: {status}")
