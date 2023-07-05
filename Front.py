accountsList = []

def newAccount(aName, aPassword, aUser):
    global accountsList
    newAccountDict = {'nome':aName, 'senha':aPassword, 'user':aUser}
    accountsList.append(newAccountDict)
def show(accountNumber):
    global accountsList
    print('Conta', accountNumber)
    thisAccountDict = accountsList[int (accountNumber)]
    print('       Nome', thisAccountDict['nome'])
    print('       Senha:', thisAccountDict['senha'])
    print('       Nome de Usuário:', thisAccountDict['user'])
    print()
def accountRecovery(accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    print('Sua senha é:', thisAccountDict['senha'])
def changeProfile(newPassword, newUser, accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    thisAccountDict['senha'] = newPassword
    thisAccountDict['user'] = newUser

def postManagement(accountNumber):
    global accountsList
    thisAccountDict = accountsList[int(accountNumber)]
    filename = f"{thisAccountDict['user']}.txt"
    with open(filename, "w") as file:
        if True:
            receita = input("")
            file.writelines(receita)
    print('Sua receita foi criada')


print ('Momesso é usúario da MoFome e seu id é', len(accountsList))
print ("\n")
newAccount("lucas", 1234, "Momesso")

print ("Olá, Bem Vindo(a) ao MoFOme, a sua rede de fanáticos gastronômicos\n")

while True:
    print ("Digite 1 para criar uma conta") #newAccount
    print ("Digite 2 para editar a sua conta") #changeProfile
    #print ("Digite 3 para adicionar seus amigos")
    print ("Digite 4 para postar uma receita") #postmanagement
    print ("Digite 5 para recuperar a sua conta") #accountRecovery
    print ("Digite 7 para ver o seu perfil") #show
    #print ("Digite 8 para ver o seu feed") 
    print ("Digite 9 para sair")

    action = input("Qual a sua opcao?")

    if action == '1':
        new_name = input ("Qual o seu Nome?\n")
        new_name = new_name.lower()
        new_password = input ("Qual será a sua senha?\n")
        new_user = input ("Digite um nome de usuário:")
        new_user = new_user.lower()
        newAccount(newAccount, new_password, new_user)
        accout_number = int (len(accountsList) - 1)
        print ('Seu id é o número', accout_number)
        print ("Conta Criada\n")

    if action == '2':
        user = input ("Digite sua conta:\n")
        passoword = input ("Digite sua senha:\n")

        print ("Conta editada\n")
    
    if action == '3':
        user = input ("Digite sua conta:\n")
        passoword = input ("Digite sua senha:\n")
        new_frend = input ("Digite o id do seu amigo:\n")
        print ("Amigo adicionado\n")
    
    if action == '4':
        id_recipe = input ("Digite seu id:\n")
        postManagement(id_recipe)
        print ("Receita postada\n")
    
    if action == '5':
        id_atual = input ("Digite seu id:\n")
        accountRecovery(id_atual)
        print ("Conta recuperada\n")
    
    if action == '9':
        print ("Até mais!!")
        break
        
