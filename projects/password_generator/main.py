import streamlit as vs
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    return "".join(random.choice(characters) for _ in range(length))

vs.title("Password Generator App 🐱‍🚀")
vs.markdown("### 😁 Generate a strong password!")

length = vs.slider("Select password length: ", min_value=6, max_value=50, value=12)

use_digits = vs.checkbox("Include Digits")

use_special =  vs.checkbox("Include Special Charactors")

if vs.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    vs.write(f"Password: {password}")

vs.write("--------------------------------------------------------------------")
vs.write("Build with 🧡 by [Vikram S](https://github.com/vikram-singh9)")
