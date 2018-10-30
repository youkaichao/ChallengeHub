import graphene

import basic.schema

class Query(basic.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
