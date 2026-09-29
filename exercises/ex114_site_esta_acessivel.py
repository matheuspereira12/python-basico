from urllib import request, error

def site_acessivel():
    try:
        resposta = request.urlopen("https://www.google.com/", timeout=5)
    except error.URLError:
        print("Não é possível acessar este site.")
    else:
        print("O site está acessível.")
        
        
site_acessivel()