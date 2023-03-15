import React from 'react';
import PropTypes from 'prop-types';
import './Alert.css';

export default function Alert({ children, type, title }) {
  return(
    <div className={`alert-wrapper ${type}`}>
      <h2>{title}</h2>
      {children}
    </div>
  )
}