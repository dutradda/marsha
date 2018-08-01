import os.path

from marsha.graphql.utils import build_executable_schema
from marsha.graphql.resolvers import resolvers

curr_dir = os.path.dirname(__file__)
schema = None

with open(os.path.join(curr_dir, 'schema.graphql')) as source:
    schema = source.read()
    schema = build_executable_schema(schema, resolvers)
