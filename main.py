import customtkinter as ct

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

janela = ct.CTk()
janela.geometry("450x280")

def click():
    print("Fazer login")

txtLogin = ct.CTkLabel(janela, text="Login")

email = ct.CTkEntry(janela, placeholder_text="E-mail")

senha = ct.CTkEntry(janela, placeholder_text="Senha", show="*")

btnLogin = ct.CTkButton(janela, text="Entrar", command=click)

txtLogin.pack(padx=10, pady=30)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
btnLogin.pack(padx=10, pady=10)

janela.mainloop()