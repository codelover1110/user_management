import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/profiles/')
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        console.error('Error fetching users:', error);
      });
  }, []);

  const handleRemove = (id) => {
    axios.delete(`http://localhost:8000/api/profiles/${id}/`)
      .then(response => {
        console.log('User deleted successfully:', response.data);
        // Update the user list after successful deletion
        setUsers(users.filter(user => user.id !== id));
      })
      .catch(error => {
        console.error('Error deleting user:', error);
      });
  };

  return (
    <div className="container mt-4">
      <h1>User List</h1>
      <Link to="/users/create" className="btn btn-primary">Create User</Link>

      <table className="table mt-3">
        <thead>
          <tr>
            <th scope="col">ID</th>
            <th scope="col">First Name</th>
            <th scope="col">Surname</th>
            <th scope="col">Email</th>
            <th scope="col">Phone</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <th scope="row">{user.id}</th>
              <td>{user.first_name}</td>
              <td>{user.surname}</td>
              <td>{user.email}</td>
              <td>{user.phone_number}</td>
              <td>
                <Link to={`/users/${user.id}/update`} className="btn btn-sm btn-outline-primary mr-1">Update</Link>
                <button onClick={() => handleRemove(user.id)} className="btn btn-sm btn-outline-danger">Remove</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default UserList;
