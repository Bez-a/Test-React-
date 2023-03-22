import React from 'react';
import PropTypes from 'prop-types';
import './Alert.css';

export default function Alert({ children, type, title }) {
  const colors = {
    success: '#6da06f',
    error: '#f56260',
  }

  const style = {
    heading: {
      color: colors[type],
      margin: '0 0 10px 0',
    },
    wrapper: {
      border: `${colors[type]} solid 1px`,
      marginBottom: 15,
      padding: 15,
      position: 'relative',
    }
  }
  return(
    <div className={`alert-wrapper ${type}`}>
      <h2>{title}</h2>
      {children}
    </div>
  )
}