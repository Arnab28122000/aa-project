"use client"

import React from 'react';
import SwaggerUI from "swagger-ui-react"
import "swagger-ui-react/swagger-ui.css"

const ApiDocumentation = () => {
  return (
    <div className='min-h-96'>
    <SwaggerUI url="http://localhost:5001/openapi.json" />
    </div>
)}

export default ApiDocumentation;
