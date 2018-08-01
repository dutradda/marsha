from marsha.graphql.utils import dict_key_resolver

def query_media_resolver(none, info):
    return {'name': 'Marsha'}


resolvers = {
    'RootQuery': {
        'media': query_media_resolver
    },
    'Media': {
        'name': dict_key_resolver('name')
    }
}
