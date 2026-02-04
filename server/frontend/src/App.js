import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register";


function App() {
  return (
    <Routes>
      {/* Route for the Login page */}
      <Route path="/login" element={<LoginPanel />} />
      
      {/* Route for the Registration page */}
      <Route path="/register" element={<Register />} />

      
      {/* Default route for the homepage/index */}
      <Route path="/" element={<div>Homepage Content</div>} />
    </Routes>
  );
}

export default App;