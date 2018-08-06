from marsha.media.media import set_stream, StreamInfo

OUTPUT = 'http://ffserver:8090/c1-48.mp3'
INPUT = '/data/10 Bem Escuro (Part. Sonianke e Mano Moreles).mp3'


def get_media_query(parent, info, id):
    return {
        'id': 1,
        'title': 'Bem Escuro'
    }


def get_media_stream_query(parent, info):
    return {'uri': OUTPUT, 'isRunning': False}


async def run_media_stream_mutation(parent, info, id):
    stream_info = StreamInfo(INPUT, OUTPUT)

    try:
        await set_stream(stream_info, False)
        return {'isRunning': True}

    except Exception as error:
        return {
            'name': type(error).__name__,
            'message': str(error)
        }


def run_media_stream_output_union(parent, info):
    return 'MediaStream'


def bulk_insert_media_mutation(parent, info):
    if not info.context['request'].files:
        return {
            'status': 'error',
            'currentCount': -1,
            'totalCount': -1,
            'error': {
                'name':  'Error',
                'message': 'Got an error'
            }
        }
    return {
        'status': 'success',
        'currentCount': 1,
        'totalCount': 1,
        'error': None
    }


def search_query(parent, info, query):
    return [get_media_query(parent, info, query)]


def searchable_union(parent, info):
    return 'Media'


resolvers = {
    'RootQuery': {
        'getMedia': get_media_query,
        'getMediaStream': get_media_stream_query,
        'search': search_query
    },
    'RootMutation': {
        'runMediaStream': run_media_stream_mutation,
        'bulkInsertMedia': bulk_insert_media_mutation
    },
    'Searchable': searchable_union,
    'RunMediaStreamOutput': run_media_stream_output_union,
    'MediaStream': {},
    'Media': {},
    'BulkInsertMediaOutput': {},
    'Error': {}
}
