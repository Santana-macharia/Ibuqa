import graphene
import api.schema
# import graphql_jwt


class Query(api.schema.Query, graphene.ObjectType):
    pass

# class Mutation(
#     api.schema.Mutation, 
#     graphene.ObjectType):
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query)

 