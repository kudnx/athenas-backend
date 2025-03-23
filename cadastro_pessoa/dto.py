from datetime import datetime

from pydantic import BaseModel


class PessoaDTO(BaseModel):
    nome: str
    data_de_nasc: datetime
    cpf: str
    sexo: str
    altura: float
    peso: float

