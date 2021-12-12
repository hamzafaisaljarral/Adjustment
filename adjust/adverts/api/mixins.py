class QueryFieldsMixin(object):
    # Split field names by this string.  It doesn't necessarily have to be a single character.
    # Avoid RFC 1738 reserved characters i.e. ';', '/', '?', ':', '@', '=' and '&'
    delimiter = ','
    group_by_field_name = 'group_by'
    include_arg_name = 'fields'

    def __init__(self, *args, **kwargs):
        super(QueryFieldsMixin, self).__init__(*args, **kwargs)

        try:
            request = self.context['request']
            method = request.method
        except (AttributeError, TypeError, KeyError):
            # The serializer was not initialized with request context.
            return

        if method != 'GET':
            return

        try:
            query_params = request.query_params
        except AttributeError:
            # DRF 2
            query_params = getattr(request, 'QUERY_PARAMS', request.GET)

        includes = query_params.getlist(self.include_arg_name)
        include_field_names = {name for names in includes for name in names.split(self.delimiter) if name}

        group_by_field = self.context['request'].GET.get(self.group_by_field_name)
        if not group_by_field:
            return

        group_by_fields = set(group_by_field.split(self.delimiter))
        excludes = set(self.context['group_by_fields']) - group_by_fields
        exclude_field_names = {name for names in excludes for name in names.split(self.delimiter) if name}

        if not exclude_field_names and not include_field_names:
            # No user fields filtering was requested, we have nothing to do here.
            return

        serializer_field_names = set(self.fields)

        fields_to_drop = serializer_field_names & exclude_field_names

        if include_field_names:
            fields_to_drop |= serializer_field_names - include_field_names

        for field in fields_to_drop:
            self.fields.pop(field)
