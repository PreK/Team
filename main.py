import menus
print("|| Menu Login\n|| 1. Utilizador\n|| 2. Admin\n|| 0. Sair")
opt=input("|| Opção:")
if opt=="1":
    menus.MenuInicial(False)
elif opt=="2":
    if input("|| Introduza a senha:")=="admin":
        menus.MenuInicial(True)
    else:
        print("|| Password errada")
elif opt=="0":
    print("|| Terminado com sucesso")
else:
    print("|| O valor introdzido é inválido")