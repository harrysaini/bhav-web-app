import React from 'react';


interface Props {

}

const LoadingSpinner: React.FunctionComponent<Props> = (props: Props) => {

    return (
      <div className="spinner-border text-primary" role="status">
        <span className="sr-only">Loading...</span>
      </div>
    );

}

export default LoadingSpinner;
