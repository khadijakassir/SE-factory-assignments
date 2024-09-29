def strong_password(p):
  hasUpper = False
  hasLower = False
  hasDigit = False
  hasSpecial = False
  specialCharacters = "#?!$"
  for char in p:
    if 'A' <= char <='Z':
      hasUpper = True
    elif 'a' <= char <= 'z':
      hasLower = True
    elif '0' <= char <= '9':
      hasDigit = True
    elif char in specialCharacters:
      hasSpecial = True 
  if len(password) >= 8 and hasUpper and hasLower and hasDigit and hasSpecial:
    return "Strong password"
  else:
    return "Weak password"

password=input(" give me your password: ")
print(strong_password(password))  