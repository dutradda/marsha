from graphql.execution.executors.asyncio import AsyncioExecutor
from sanic import Sanic
from sanic_graphql import GraphQLView
from sanic_cors import CORS, cross_origin

from marsha.graphql.schema import schema

app = Sanic()
CORS(app, resources={'/graphql': {"origins": "*"}}, automatic_options=True)


@app.listener('before_server_start')
def init_graphql(app, loop):
    app.add_route(
        GraphQLView.as_view(
            schema=schema,
            executor=AsyncioExecutor(loop=loop),
            graphiql=True
        ),
        '/graphql'
    )
