import React from 'react'; 
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'; 
import LoginPage from './pages/LoginPage.jsx'; 
import SignupPage from './pages/SignupPage.jsx'; 
import AnimalsPage from './pages/AnimalsPage.jsx';
import HomePage from './pages/HomePage.jsx'; 

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow-md py-4">
          <ul className="flex justify-center space-x-4">
            <li><Link to="/" className="text-blue-500 hover:text-blue-700">Home</Link></li>
            <li><Link to="/login" className="text-blue-500 hover:text-blue-700">Login</Link></li>
            <li><Link to="/signup" className="text-blue-500 hover:text-blue-700">Signup</Link></li>
            <li><Link to="/animals" className="text-black-500 hover:text-red-700">Animals</Link></li>
          </ul>
        </nav>
        <main className="container mx-auto py-8">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/animals" element={<AnimalsPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
