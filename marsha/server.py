from sanic import Sanic
from sanic_graphql import GraphQLView

from marsha.graphql.schema import schema

app = Sanic()
app.add_route(GraphQLView.as_view(schema=schema, graphiql=True), '/graphql')
