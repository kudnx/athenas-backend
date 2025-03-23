from cadastro_pessoa.dto import PessoaDTO
from cadastro_pessoa.models import Pessoa


class PessoaTask:

    @staticmethod
    def criar_pessoa(pessoa: PessoaDTO):
        return Pessoa.objects.create(nome=pessoa.nome, data_de_nasc=pessoa.data_de_nasc, cpf=pessoa.cpf, sexo=pessoa.sexo, altura=pessoa.altura, peso=pessoa.peso)

    @staticmethod
    def listar_pessoas():
        return Pessoa.objects.all()

    @staticmethod
    def pesquisar_pessoas_por_nome(pessoa_nome: str):
        return Pessoa.objects.filter(nome__icontains=pessoa_nome)

    @staticmethod
    def listar_pessoa_por_id(pessoa_id: int):
        return Pessoa.objects.get(id=pessoa_id)

    @staticmethod
    def atualizar_pessoa(request, id: int):
        pessoa = Pessoa.objects.get(id=id)
        pessoa.nome = request.data.get('nome')
        pessoa.data_de_nasc = request.data.get('data_de_nasc')
        pessoa.cpf = request.data.get('cpf')
        pessoa.sexo = request.data.get('sexo')
        pessoa.altura = request.data.get('altura')
        pessoa.peso = request.data.get('peso')
        pessoa.save()
        return pessoa

    @staticmethod
    def deletar_pessoa(pessoa_id: int) -> str:
        pessoa = Pessoa.objects.get(id=pessoa_id)
        nome = pessoa.nome
        pessoa.delete()
        return nome

    @staticmethod
    def calcular_imc(pessoa_id: int):
        pessoa = Pessoa.objects.get(id=pessoa_id)
        if pessoa.sexo == 'M':
            imc = float(pessoa.peso * pessoa.altura) - 58
        else:
            imc = float(pessoa.peso * pessoa.altura) - 44.7
        return round(imc, 2)


