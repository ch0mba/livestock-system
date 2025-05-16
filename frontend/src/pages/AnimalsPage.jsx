import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const AnimalsPage = () => {
    const [animals, setAnimals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [showAddForm, setShowAddForm] = useState(false);
    const [newAnimal, setNewAnimal] = useState({
        rfid: '',
        type: '',
        breed: '',
        birthdate: '',
    });
    const navigate = useNavigate();

    const fetchAnimals = async () => {
        setLoading(true);
        setError(null);
        try {
            const token = localStorage.getItem('authToken');
            if (!token) {
                navigate('/login');
                return;
            }
            const response = await axios.get('/api/animals/', {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            setAnimals(response.data);
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchAnimals();
    }, []);

    const handleAddAnimal = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('authToken');
            if (!token) {
                navigate('/login');
                return;
            }
            await axios.post('http://127.0.0.1:8000/api/animals/', newAnimal, {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            fetchAnimals(); // Refresh the list after adding
            setShowAddForm(false); // Hide the form
            setNewAnimal({ rfid: '', type: '', breed: '', birthdate: '' }); // Reset the form
        } catch (error) {
            setError(error);
        }
    };

    const handleDeleteAnimal = async (rfid) => {
        try {
            const token = localStorage.getItem('authToken');
            if (!token) {
                navigate('/login');
                return;
            }
            await axios.delete(`/api/animals/${rfid}/`, {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            fetchAnimals(); // Refresh the list after deleting
        } catch (error) {
            setError(error);
        }
    };

    if (loading) {
        return <div>Loading animals...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-3xl font-bold mb-4">Animals</h1>
            <button
                className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mb-4"
                onClick={() => setShowAddForm(!showAddForm)}
            >
                {showAddForm ? 'Cancel' : 'Add Animal'}
            </button>

            {showAddForm && (
                <form onSubmit={handleAddAnimal} className="bg-white shadow-md rounded-lg p-6 mb-4">
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="rfid">RFID:</label>
                        <input
                            type="text"
                            id="rfid"
                            value={newAnimal.rfid}
                            onChange={(e) => setNewAnimal({ ...newAnimal, rfid: e.target.value })}
                            required
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="type">Type:</label>
                        <input
                            type="text"
                            id="type"
                            value={newAnimal.type}
                            onChange={(e) => setNewAnimal({ ...newAnimal, type: e.target.value })}
                            required
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="breed">Breed:</label>
                        <input
                            type="text"
                            id="breed"
                            value={newAnimal.breed}
                            onChange={(e) => setNewAnimal({ ...newAnimal, breed: e.target.value })}
                            required
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="birthdate">Birthdate:</label>
                        <input
                            type="date"
                            id="birthdate"
                            value={newAnimal.birthdate}
                            onChange={(e) => setNewAnimal({ ...newAnimal, birthdate: e.target.value })}
                            required
                            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        />
                    </div>
                    <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
                        Add Animal
                    </button>
                </form>
            )}

            <div className="bg-white shadow-md rounded-lg p-4">
                {Array.isArray(animals) ? (
                    animals.length === 0 ? (
                        <p className="text-gray-500">No animals found.</p>
                    ) : (
                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    
                                <div key={animal.rfid} className="border rounded-lg p-4">
                                    <h2 className="text-xl font-semibold">{animal.type} - {animal.breed}</h2>
                                    <p>RFID: {animal.rfid}</p>
                                    <p>Birthdate: {animal.birthdate}</p>
                                    <button
                                        className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mt-2"
                                        onClick={() => handleDeleteAnimal(animal.rfid)}
                                    >
                                        Delete
                                    </button>
                                </div>
                            
                        </div>
                    )
                ) : null}
            </div>
        </div>
    );
};

export default AnimalsPage;