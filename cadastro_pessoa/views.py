# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pessoa
from .serializers import PessoaSerializer
from .service import PessoaService


class PessoaControler(APIView):

    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    @staticmethod
    @api_view(['GET'])
    def get(request, pessoa_id: int = None, pessoa_nome: str = None):
        if pessoa_id:
            pessoa_service = PessoaService()
            pessoa = pessoa_service.listar_pessoa_por_id(pessoa_id=pessoa_id)
            return Response(pessoa.data, status=200)
        pessoa_service = PessoaService()
        pessoa = pessoa_service.listar_pessoas(request)
        return Response(pessoa.data, status=200)

    @staticmethod
    @api_view(['GET'])
    def get_pessoas(request, pessoa_nome: str):
        pessoa_service = PessoaService()
        pessoa = pessoa_service.pesquisar_pessoas_por_nome(pessoa_nome=pessoa_nome)
        return Response(pessoa.data, status=200)

    @staticmethod
    @api_view(['POST'])
    def post(request):
        pessoa_service = PessoaService()
        pessoa_service.cadastrar_pessoa(request.data)
        return Response("Pessoa cadastrada com Sucesso!!", status=200)

    @staticmethod
    @api_view(['PUT'])
    def put(request, pessoa_id: int):
        pessoa_service = PessoaService()
        pessoa_service.atualizar_pessoa(request=request, id=pessoa_id)
        return Response("Pessoa atualizada com Sucesso!!", status=200)

    @staticmethod
    @api_view(['DELETE'])
    def delete(request, pessoa_id: int):
        pessoa_service = PessoaService()
        nome_da_pessoa_deletada = pessoa_service.deletar_pessoa(pessoa_id=pessoa_id)
        return Response(f"A pessoa com o nome de {nome_da_pessoa_deletada} foi deletada com Sucesso!!", status=200)

    @staticmethod
    @api_view(['GET'])
    def calcular_imc(request, pessoa_id: int):
        pessoa_service = PessoaService()
        imc = pessoa_service.calcular_imc(pessoa_id=pessoa_id)
        return Response(f"O IMC é: {imc}", status=200)
