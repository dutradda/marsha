from collections import namedtuple

from marsha.graphql.utils import build_sqlalchemy_models
from marsha.graphql.schema import schema

SQLAlchBuilderInput = namedtuple(
    'SQLAlchBuilderInput',
    ['name', 'super', 'is_abstract', 'abstract_attrs']
)

builderInputs = [
    SQLAlchBuilderInput('Media'),
    SQLAlchBuilderInput('Person'),
    SQLAlchBuilderInput('GroupOfPeople'),
    SQLAlchBuilderInput('Collection'),
    SQLAlchBuilderInput('MediaStream')
]

models = build_sqlalchemy_models(builderInputs, schema)