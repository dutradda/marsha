import graphql
import os.path

curr_dir = os.path.dirname(__file__)
ast = None

with open(os.path.join(curr_dir, 'schema.graphql')) as source:
    schema = source.read()
    ast = graphql.parse(schema)

schema = graphql.build_ast_schema(ast)

schema.get_type('RootQuery').fields['media'].resolver = lambda *a, **k: 1
schema.get_type('Media').fields['name'].resolver = lambda *a, **k: 'Marsha'
