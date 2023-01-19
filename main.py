import graphene
from fastapi import FastAPI

app = FastAPI()


class Query(graphene.ObjectType):
    a=""
    def resolve_title(root, info):
        return "Yuvraj"
    def resolve_age(root, info):
        return '22'

schema =graphene.Schema(query=Query)
query_gaphql='''
query get {
    name
    age
}
'''

result = schema.execute(query_gaphql)