import React, {useState} from 'react';
import PropTypes from 'prop-types';
import Viewer from '@samvera/clover-iiif/viewer';

/**
 * The Cloveriiif component takes one parameter 'iiifLink'.
 * If an iiifLink is not passed in, then it will be set to the
 * default image "Crossing the Pend d'Oreille - Kalispel".
 */
const Cloveriiif = (props) => {
    const {iiifLink} = props;

    return (
        <div>
            <Viewer
                iiifContent={
                    iiifLink ??
                    'https://api.dc.library.northwestern.edu/api/v2/works/8a833741-74a8-40dc-bd1d-c416a3b1bb38?as=iiif'
                }
            />
        </div>
    );
};

Cloveriiif.defaultProps = {};

Cloveriiif.propTypes = {
    /**
     * The link to the iiif image.
     */
    iiifLink: PropTypes.string,
};

export default Cloveriiif;
