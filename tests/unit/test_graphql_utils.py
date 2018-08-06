from marsha.graphql.utils import build_executable_schema
from graphql import GraphQLSchema

import pytest



@pytest.fixture
def simple_schema():
    return """
        schema {
            query: Query
        }
        type Query {
            get: String
        }
    """


def test_build_executable_schema(simple_schema):
    resolvers = {
        'Query': {
            'get': lambda parent, info: 'got'
        }
    }
    schema = build_executable_schema(simple_schema, resolvers)

    assert isinstance(schema, GraphQLSchema)


def test_build_executable_schema_with_empty_resolvers(simple_schema):
    with pytest.raises(ValueError) as exc_info:
        schema = build_executable_schema(simple_schema, {})

    assert exc_info.value.args == ("resolvers can't be empty",)
