# AUTO GENERATED FILE - DO NOT EDIT

#' @export
cloveriiif <- function(iiifLink=NULL) {
    
    props <- list(iiifLink=iiifLink)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Cloveriiif',
        namespace = 'cloveriiif',
        propNames = c('iiifLink'),
        package = 'cloveriiif'
        )

    structure(component, class = c('dash_component', 'list'))
}
