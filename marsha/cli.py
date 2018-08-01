import graphql
import json
from schema import schema

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
    print(json.dumps(query_result.data, indent=4))
    print()


if __name__ == '__main__':
    main()
