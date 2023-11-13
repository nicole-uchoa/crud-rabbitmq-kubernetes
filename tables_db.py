from pydantic import BaseModel

# O plano de saúde
class Operadora(BaseModel):
    nome: str
    cnpj: str

# O hospital ou clínica médica 
# Um prestador pode ter mais de uma operadora e pode estar em mais de uma cidade
class Prestador(BaseModel):
    nome : str
    cnpj : str
    cidade : str
    estado: str

# O procedimento pode ter valores diferentes de acordo com o prestador e operadora
class Procedimento(BaseModel):
    descricao : str
    valor : float
    operadora_id: int

class Beneficiario(BaseModel):
    nome : str
    num_carteira : str
    cidade : str
    estado: str
    procedimento_id :int
    prestador_id: int


