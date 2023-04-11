import secrets
import string
import pyperclip

# code imported from local sandbox

def generate_pwd(pw_length, alphabet, special_chars, digits):
    pwd_strong = False
    while not pwd_strong:
        pwd = ''
        for x in range(pw_length):
            # select random item from alphabet | append to pwd string
            pwd += ''.join(secrets.choice(alphabet))
        # check pwd for special characters and numbers 
        has_special_chars = any(char in special_chars for char in pwd)
        has_min_nums = sum(char in digits for char in pwd) >= 3

        if (has_special_chars and has_min_nums):
            # meets reqs -> turn pwd string flag to True
            pwd_strong = True                   
    return pwd

def create_pw(pw_length):
    digits = string.digits
    special_chars = string.punctuation
    letters = string.ascii_letters

    # collection of alphabet (lower & uppercase) | digits 0-9 | standard special chars
    alphabet = letters + digits + special_chars
    pwd = generate_pwd(pw_length, alphabet, special_chars, digits)
    return pwd

def run_pw_gen():
   print('Welcome to Password Generator!')
   # data type validation | program can only accept integers
   try:
      pwd_length = int(input('Please enter your desired password length (8-25 / integers only), then press enter: '))
   except Exception:
      print('Invalid entry. Please enter an integer between 8 and 25.')
   else:
      # more validation | pwd_length must be 1-25
      if pwd_length < 26 and pwd_length > 7:
         pwd = create_pw(pwd_length)
         print(f'Your New Password is: {pwd}\nPassword Length: {len(pwd)}')
         # copy password to user clipboard
         pyperclip.copy(pwd)
         print('New password copied to clipboard!')
      else:
         print('Invalid entry. Please enter an integer between 8 and 25.')

run_pw_gen()