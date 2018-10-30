import graphene
import basic.schema


class Query(basic.schema.Query, graphene.ObjectType):
    pass


class Mutation(basic.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
