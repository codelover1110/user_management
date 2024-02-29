import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

function CreateUser() {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    first_name: '',
    surname: '',
    email: '',
    phone_number: '',
  });
  const [errorMessages, setErrorMessages] = useState({});

  const handleChange = (e) => {
    setUserData({
      ...userData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/profiles/', userData);

      console.log('User created successfully:', response.data);
      // Redirect to user list after successful creation
      navigate('/users');
    } catch (error) {
      console.error('Error creating user:', error);

      // If there are error messages from the backend, display them as alerts
      if (error.response && error.response.data) {
        setErrorMessages(error.response.data);
      } else {
        alert('An error occurred while creating the user.');
      }
    }
  };

  return (
    <div className="container mt-4">
      <h1>Create User</h1>
      <Link to="/users" className="btn btn-secondary">Back to User List</Link>
      <form onSubmit={handleSubmit} className="mt-3">
        <div className="form-group">
          <label>First Name:</label>
          <input type="text" name="first_name" className="form-control" value={userData.first_name} onChange={handleChange} />
        </div>

        <div className="form-group">
          <label>Surname:</label>
          <input type="text" name="surname" className="form-control" value={userData.surname} onChange={handleChange} />
        </div>

        <div className="form-group">
          <label>Email:</label>
          <input type="email" name="email" className="form-control" value={userData.email} onChange={handleChange} />
          {errorMessages.email && <div className="alert alert-danger mt-2" role="alert">{errorMessages.email}</div>}
        </div>

        <div className="form-group">
          <label>Phone Number:</label>
          <input type="text" name="phone_number" className="form-control" value={userData.phone_number} onChange={handleChange} />
          {errorMessages.phone_number && <div className="alert alert-danger mt-2" role="alert">{errorMessages.phone_number}</div>}
        </div>

        <button type="submit" className="btn btn-primary">Create User</button>
      </form>
    </div>
  );
}

export default CreateUser;
