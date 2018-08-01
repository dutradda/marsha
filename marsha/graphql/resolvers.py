from marsha.graphql.utils import dict_key_resolver
from marsha.media.media import set_stream, StreamInfo

OUTPUT = 'http://ffserver:8090/c1-48.mp3'
INPUT = '/data/10 Bem Escuro (Part. Sonianke e Mano Moreles).mp3'

def query_media_resolver(none, info):
    return {'url': OUTPUT}


async def start_media_streaming_resolver(none, info):
    media_streaming = {'isRunning': True, 'errorMsg': ''}
    stream_info = StreamInfo(INPUT, OUTPUT)

    try:
        await set_stream(stream_info, False)
    except Exception as error:
        media_streaming['isRunning'] = False
        media_streaming['errorMsg'] = str(error)

    return media_streaming


resolvers = {
    'RootQuery': {
        'media': query_media_resolver
    },
    'Media': {
        'url': dict_key_resolver('url')
    },
    'RootMutation': {
        'startMediaStreaming': start_media_streaming_resolver
    },
    'MediaStreaming': {
        'isRunning': dict_key_resolver('isRunning'),
        'errorMsg': dict_key_resolver('errorMsg')
    }
}
