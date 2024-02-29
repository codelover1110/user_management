import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UserList from './UserList';
import CreateUser from './CreateUser';
import UpdateUser from './UpdateUser';
import RemoveUser from './RemoveUser';

function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/users" element={<UserList />} />
        <Route path="/users/create" element={<CreateUser />} />
        <Route path="/users/:id/update" element={<UpdateUser />} />
        <Route path="/users/:id/remove" element={<RemoveUser />} />
      </Routes>
    </Router>
  );
}

export default AppRouter;
