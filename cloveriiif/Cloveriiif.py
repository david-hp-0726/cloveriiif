# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Cloveriiif(Component):
    """A Cloveriiif component.
The Cloveriiif component takes one parameter 'iiifLink'.
If an iiifLink is not passed in, then it will be set to the
default image "Crossing the Pend d'Oreille - Kalispel".

Keyword arguments:

- iiifLink (string; optional):
    The link to the iiif image."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'cloveriiif'
    _type = 'Cloveriiif'
    @_explicitize_args
    def __init__(self, iiifLink=Component.UNDEFINED, **kwargs):
        self._prop_names = ['iiifLink']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['iiifLink']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Cloveriiif, self).__init__(**args)
