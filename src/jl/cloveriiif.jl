# AUTO GENERATED FILE - DO NOT EDIT

export cloveriiif

"""
    cloveriiif(;kwargs...)

A Cloveriiif component.
The Cloveriiif component takes one parameter 'iiifLink'.
If an iiifLink is not passed in, then it will be set to the
default image "Crossing the Pend d'Oreille - Kalispel".
Keyword arguments:
- `iiifLink` (String; optional): The link to the iiif image.
"""
function cloveriiif(; kwargs...)
        available_props = Symbol[:iiifLink]
        wild_props = Symbol[]
        return Component("cloveriiif", "Cloveriiif", "cloveriiif", available_props, wild_props; kwargs...)
end

