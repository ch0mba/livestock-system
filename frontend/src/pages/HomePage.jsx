import React from 'react';

const HomePage = () => {
  const username = localStorage.getItem('username');

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-4 text-center text-gray-800">
          Welcome to the Livestock Management System
        </h1>
        {username && <p className="text-lg text-center text-green-600">Welcome, {username}!</p>}
        <p className="text-gray-700 text-center mt-4">This is your personalized homepage.</p>
        {/* Add more homepage content here, styled with Tailwind */}
      </div>
    </div>
  );
};

export default HomePage;