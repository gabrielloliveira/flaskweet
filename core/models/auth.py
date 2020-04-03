from .tables import User
from .utils import verify


def authenticate(username, password):
    """
    Função para saber se o usuário está apto para fazer login.

    Parâmetros:
        username: nome do usuário.
        password: senha que o usuário informou.

    Retorno:
        Retorna o objeto usuário caso tenha informado as credenciais corretas. 
        Caso contrário, retorna Falso.
    """
    user = User.query.filter_by(username=username).first()
    if user is None or not verify(password, user.password):
        return False

    return user
