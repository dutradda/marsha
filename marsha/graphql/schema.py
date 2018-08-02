import os.path

from marsha.graphql.utils import build_executable_schema
from marsha.graphql.resolvers import resolvers

curr_dir = os.path.dirname(__file__)
schema = ''

for filename in ['schema.graphql', '../media/schema.graphql']:
    with open(os.path.join(curr_dir, filename)) as source:
        schema_i = source.read()
        schema += schema_i + '\n'

schema = build_executable_schema(schema, resolvers)
