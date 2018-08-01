import graphql
import ujson
from marsha.schema import schema

query = \
"""
query Marsha {
    media {
        name
    }
}
"""

def main():
    query_result = graphql.graphql(schema, query)
    print(ujson.dumps(query_result.data, indent=4))
    print()


if __name__ == '__main__':
    main()
