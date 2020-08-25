from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class Identifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'pid'
    template = 'P{device_id}{random_string}'
