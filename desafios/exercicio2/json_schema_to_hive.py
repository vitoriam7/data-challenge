import json
import boto3
from json2hive.utils import infer_schema
from json2hive.generators import generate_json_table_statement

_ATHENA_CLIENT = None

def create_hive_table_with_athena(query):
    '''
    Função necessária para criação da tabela HIVE na AWS
    :param query: Script SQL de Create Table (str)
    :return: None
    '''
    
    print(f"Query: {query}")
    _ATHENA_CLIENT.start_query_execution(
        QueryString=query,
        ResultConfiguration={
            'OutputLocation': f's3://iti-query-results/'
        }
    )

def handler():
    '''
    #  Função principal
    Aqui você deve começar a implementar o seu código
    Você pode criar funções/classes à vontade
    Utilize a função create_hive_table_with_athena para te auxiliar
        na criação da tabela HIVE, não é necessário alterá-la
    '''
    f = open('C:/Users/Host/Documents/git/data-challenge/data-challenge/desafios/exercicio2/schema.json')
    schema_template = json.load(f)

def json_attributes(schema_template):

    schema_template = schema_template
    column_names = (c for c in schema_template['name'])
    #column_types = (i for i in schema_template['type'])
    print(column_names)

        

