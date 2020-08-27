from edc_identifier.simple_identifier import SimpleUniqueIdentifier


class EmployeeIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'pid'
    template = 'E{device_id}{random_string}'


class ConsultantIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'pid'
    template = 'C{device_id}{random_string}'


class PiIdentifier(SimpleUniqueIdentifier):

    random_string_length = 5
    identifier_type = 'pid'
    template = 'P{device_id}{random_string}'
