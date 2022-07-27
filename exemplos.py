
# testando decoradores

def uma_funcao():
    print("uma_funcao")
    
def outra_funcao(func):
    print("outra_funcao")
    func()
    
    
outra_funcao(uma_funcao)


def uma_funcao_com_args(param):
    print('uma_funcao param {}'.format(param))
    
def outra_funcao(func, *args):
    print('irem chamar {}'.format(func.__name__))
    return func(*args)
    