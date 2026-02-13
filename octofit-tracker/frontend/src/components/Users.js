import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Users - Fetching from API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Users - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        console.log('Users - Processed data:', usersData);
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Users - Error fetching data:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="container mt-4 text-center">
        <div className="spinner-border spinner-border-custom text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <p className="mt-3 text-muted">Loading users...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-4">
        <div className="alert alert-danger d-flex align-items-center" role="alert">
          <i className="bi bi-exclamation-triangle-fill me-2"></i>
          <div>
            <strong>Error:</strong> {error}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>
          <i className="bi bi-person-circle me-2"></i>
          Users
        </h2>
        <span className="badge bg-success">{users.length} Members</span>
      </div>
      
      {users.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle-fill me-2"></i>
          No users found.
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead>
              <tr>
                <th><i className="bi bi-image me-1"></i>Avatar</th>
                <th><i className="bi bi-person me-1"></i>Username</th>
                <th><i className="bi bi-envelope me-1"></i>Email</th>
                <th><i className="bi bi-people me-1"></i>Team</th>
                <th><i className="bi bi-calendar-check me-1"></i>Date Joined</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr key={user.id}>
                  <td>
                    <img 
                      src={user.avatar_url || '/avatars/default.svg'} 
                      alt={user.username}
                      className="avatar-img"
                      onError={(e) => { e.target.style.display = 'none'; }}
                    />
                  </td>
                  <td>
                    <strong><i className="bi bi-person-badge me-1"></i>{user.username}</strong>
                  </td>
                  <td>{user.email}</td>
                  <td>
                    {user.team ? (
                      <span className="badge bg-info">{user.team}</span>
                    ) : (
                      <span className="text-muted">No team</span>
                    )}
                  </td>
                  <td>{new Date(user.created_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Users;
