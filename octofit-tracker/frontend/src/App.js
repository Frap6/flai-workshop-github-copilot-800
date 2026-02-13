import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from './octofitapp-small.png';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            <img src={logo} alt="OctoFit Logo" className="navbar-logo" />
            OctoFit Tracker
          </Link>
          <button 
            className="navbar-toggler" 
            type="button" 
            data-bs-toggle="collapse" 
            data-bs-target="#navbarNav" 
            aria-controls="navbarNav" 
            aria-expanded="false" 
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <Routes>
        <Route path="/" element={
          <div className="container mt-4">
            <div className="hero-section text-center">
              <h1 className="display-4 fw-bold mb-3">
                <i className="bi bi-heart-pulse-fill me-3"></i>
                Welcome to OctoFit Tracker
              </h1>
              <p className="lead">Track your fitness activities, compete with teams, and get personalized workout suggestions.</p>
            </div>
            
            <div className="row g-4">
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-person-circle feature-icon"></i>
                  <h3>User Profiles</h3>
                  <p className="text-muted">Create and manage your personal fitness profile</p>
                  <Link to="/users" className="btn btn-primary">View Users</Link>
                </div>
              </div>
              
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-activity feature-icon"></i>
                  <h3>Track Activities</h3>
                  <p className="text-muted">Log your workouts and monitor your progress</p>
                  <Link to="/activities" className="btn btn-primary">View Activities</Link>
                </div>
              </div>
              
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-people-fill feature-icon"></i>
                  <h3>Join Teams</h3>
                  <p className="text-muted">Collaborate and compete with your fitness team</p>
                  <Link to="/teams" className="btn btn-primary">View Teams</Link>
                </div>
              </div>
              
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-trophy-fill feature-icon"></i>
                  <h3>Leaderboard</h3>
                  <p className="text-muted">See how you rank among other users</p>
                  <Link to="/leaderboard" className="btn btn-primary">View Rankings</Link>
                </div>
              </div>
              
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-lightning-charge-fill feature-icon"></i>
                  <h3>Workout Plans</h3>
                  <p className="text-muted">Get personalized workout suggestions</p>
                  <Link to="/workouts" className="btn btn-primary">View Workouts</Link>
                </div>
              </div>
              
              <div className="col-md-4">
                <div className="feature-card">
                  <i className="bi bi-graph-up-arrow feature-icon"></i>
                  <h3>Track Progress</h3>
                  <p className="text-muted">Monitor your fitness journey over time</p>
                  <Link to="/activities" className="btn btn-primary">See Progress</Link>
                </div>
              </div>
            </div>
          </div>
        } />
        <Route path="/users" element={<Users />} />
        <Route path="/activities" element={<Activities />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
