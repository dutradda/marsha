from marsha.graphql.utils import dict_key_resolver
from marsha.media.media import set_stream, StreamInfo

OUTPUT = 'http://ffserver:8090/c1-48.mp3'
INPUT = '/data/10 Bem Escuro (Part. Sonianke e Mano Moreles).mp3'


def get_media(parent, info, id):
    return {'title': 'Bem Escuro'}


def get_media_stream(parent, info):
    return {'uri': OUTPUT, 'isRunning': False}


async def run_media_stream(parent, info, id):
    stream_info = StreamInfo(INPUT, OUTPUT)

    try:
        await set_stream(stream_info, False)
        return {'isRunning': True}

    except Exception as error:
        return {
            'name': type(error).__name__,
            'message': str(error)
        }


def run_media_stream_output(parent, info):
    return 'MediaStream'


resolvers = {
    'RootQuery': {
        'getMedia': get_media,
        'getMediaStream': get_media_stream
    },
    'Media': {
        'title': dict_key_resolver('title')
    },
    'MediaStream': {
        'uri': dict_key_resolver('uri'),
        'isRunning': dict_key_resolver('isRunning')
    },
    'RootMutation': {
        'runMediaStream': run_media_stream
    },
    'RunMediaStreamOutput': run_media_stream_output,
    'Error': {
        'name': dict_key_resolver('name'),
        'message': dict_key_resolver('message')
    }
}
