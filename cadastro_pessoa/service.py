from cadastro_pessoa.dto import PessoaDTO
from cadastro_pessoa.serializers import PessoaSerializer
from cadastro_pessoa.tasks import PessoaTask


class PessoaService:

    @staticmethod
    def cadastrar_pessoa(pessoa):
        pessoa_dto = PessoaDTO(**pessoa)
        return PessoaTask.criar_pessoa(pessoa_dto)

    @staticmethod
    def listar_pessoas(request):
        pessoa = PessoaTask.listar_pessoas()
        pessoa_serializer = PessoaSerializer(pessoa, many=True, context={'request': request})
        return pessoa_serializer

    @staticmethod
    def listar_pessoa_por_id(pessoa_id):
        pessoa = PessoaTask.listar_pessoa_por_id(pessoa_id=pessoa_id)

        pessoa_serializer = PessoaSerializer(pessoa, many=False, context={'request': None})

        return pessoa_serializer

    @staticmethod
    def pesquisar_pessoas_por_nome(pessoa_nome):
        pessoa = PessoaTask.pesquisar_pessoas_por_nome(pessoa_nome=pessoa_nome)
        pessoa_serializer = PessoaSerializer(pessoa, many=True, context={'request': None})
        return pessoa_serializer

    @staticmethod
    def atualizar_pessoa(request, id: int):
        return PessoaTask.atualizar_pessoa(request=request, id=id)

    @staticmethod
    def deletar_pessoa(pessoa_id: int) -> str:
        return PessoaTask.deletar_pessoa(pessoa_id=pessoa_id)

    @staticmethod
    def calcular_imc(pessoa_id: int):
        return PessoaTask.calcular_imc(pessoa_id=pessoa_id)
