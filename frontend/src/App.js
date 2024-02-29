import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import UserList from './components/UserList';
import CreateUser from './components/CreateUser';
import UpdateUser from './components/UpdateUser';
import RemoveUser from './components/RemoveUser';

function App() {
  return (
    <Router>
      <div className="container">
        <div className="header">
          <h1>My Simple React App</h1>
        </div>
        
        <Route path="/" exact component={UserList} />
        <Route path="/create" component={CreateUser} />
        <Route path="/update/:id" component={UpdateUser} />
        <Route path="/remove/:id" component={RemoveUser} />
      </div>
    </Router>
  );
}

export default App;
