
# testando decoradores

def uma_funcao():
    print("uma_funcao")
    
def outra_funcao(func):
    print("outra_funcao")
    func()
    
    
outra_funcao(uma_funcao)