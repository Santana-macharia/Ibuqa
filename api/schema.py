import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Customers

class CustomersType(DjangoObjectType):
    class Meta:
        model = Customers

class Query(graphene.ObjectType):
    customers = graphene.List(CustomersType, search=graphene.String())

    def resolve_customers(self, info, search=None):
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(code__icontains=search) 
                
            )
            return Customers.objects.filter(filter)

        return Customers.objects.all()

class CreateCustomers(graphene.Mutation):
    customers = graphene.Field(CustomersType)

    class Arguments:
        name = graphene.String()
        code = graphene.Int()
    

    def mutate(self, info, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("user must logged in to create a customer")

        customers = Customers(name=kwargs.get('name'), code=kwargs.get('code'))

        customers.save()
        return CreateCustomers(customers=customers)

class UpdateCustomers(graphene.Mutation):
    customers = graphene.Field(CustomersType)

    class Arguments:
        name = graphene.String()
        code = graphene.Int()

    def mutate(self, info, name=None, code=None):
        user = info.context.user
        customers = Customers.objects.get(code=code)

        if user.is_anonymous:
            raise GraphQLError("user must logged in to update a customer. Also user must be the creator")

        customers.name = name if name != None and name != "" else customers.name
        customers.code = code if code != None and code != "" else customers.code
        

        customers.save()

        return UpdateCustomers(customers=customers)

class DeleteCustomers(graphene.Mutation):
    code = graphene.Int()

    class Arguments:
        code = graphene.Int(required=True)

    def mutate(self, info, code):
        user = info.context.user
        customers = Customers.objects.get(code=code)

        if user.is_anonymous:
            raise GraphQLError("user must logged in to update a customer. Also user must be the creator")

        customers.delete()

        return DeleteCustomers(code=code)


class Mutation(graphene.ObjectType):
    create_customers = CreateCustomers.Field()
    update_customers = UpdateCustomers.Field()
    delete_customers = DeleteCustomers.Field()