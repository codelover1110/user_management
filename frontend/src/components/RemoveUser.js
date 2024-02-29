import React, { useState, useEffect } from 'react';
import { Link, useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

function RemoveUser() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    first_name: '',
    surname: '',
    email: '',
    phone_number: '',
  });

  useEffect(() => {
    axios.get(`http://localhost:8000/api/profiles/${id}/`)
      .then(response => {
        setUserData(response.data);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, [id]);

  const handleRemove = () => {
    axios.delete(`http://localhost:8000/api/profiles/${id}/`)
      .then(response => {
        console.log('User deleted successfully:', response.data);
        navigate('/users');
      })
      .catch(error => {
        console.error('Error deleting user:', error);
      });
  };

  return (
    <div className="container mt-4">
      <h1>Remove User</h1>
      <Link to="/users" className="btn btn-secondary">Back to User List</Link>
      <p className="mt-3">Are you sure you want to remove the user {userData.first_name} {userData.surname}?</p>
      <button onClick={handleRemove} className="btn btn-danger">Remove User</button>
    </div>
  );
}

export default RemoveUser;
