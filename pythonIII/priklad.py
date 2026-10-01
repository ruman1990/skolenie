import secrets
import string

abeceda = "abcdefgijklmnoprstuvyzqwxABCDEFGHIJKLMNOPRS" + "0123456789" + "!@#$%^&*"
heslo = ''.join(secrets.choice(abeceda) for _ in range(12))
print(heslo)  # napr. 'b7V$u19@GwLs'