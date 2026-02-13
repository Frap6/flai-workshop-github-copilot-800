import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Helper function to get avatar URL from username
  const getAvatarUrl = (username) => {
    return `/avatars/${username}.svg`;
  };

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams - Fetching from API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams - Processed data:', teamsData);
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Teams - Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading teams...</p>
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
          <i className="bi bi-people-fill me-2"></i>
          Teams
        </h2>
        <span className="badge bg-info">{teams.length} Teams</span>
      </div>
      
      {teams.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle-fill me-2"></i>
          No teams found. Create a team to get started!
        </div>
      ) : (
        <div className="row g-4">
          {teams.map((team) => (
            <div key={team.id} className="col-md-6 col-lg-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">
                    <i className="bi bi-flag-fill me-2 text-primary"></i>
                    {team.name}
                  </h5>
                  <p className="card-text flex-grow-1">{team.description}</p>
                  
                  {/* Team Captain */}
                  {team.captain && (
                    <div className="mb-3">
                      <small className="text-muted fw-bold">
                        <i className="bi bi-star-fill me-1 text-warning"></i>
                        Captain:
                      </small>
                      <div className="d-flex align-items-center mt-1">
                        <img 
                          src={getAvatarUrl(team.captain)} 
                          alt={team.captain}
                          className="avatar-img-small me-2"
                          onError={(e) => { e.target.style.display = 'none'; }}
                        />
                        <span className="badge bg-warning text-dark">{team.captain}</span>
                      </div>
                    </div>
                  )}
                  
                  {/* Team Members */}
                  {team.members && team.members.length > 0 && (
                    <div className="mb-3">
                      <small className="text-muted fw-bold">
                        <i className="bi bi-people-fill me-1"></i>
                        Members ({team.members.length}):
                      </small>
                      <div className="d-flex flex-wrap gap-2 mt-2">
                        {team.members.map((member, idx) => (
                          <div key={idx} className="d-flex flex-column align-items-center">
                            <img 
                              src={getAvatarUrl(member)} 
                              alt={member}
                              className="avatar-img-small"
                              onError={(e) => { e.target.style.display = 'none'; }}
                              title={member}
                            />
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                  
                  {/* Team Points */}
                  {team.total_points !== undefined && (
                    <div className="mb-2">
                      <span className="badge bg-success">
                        <i className="bi bi-trophy-fill me-1"></i>
                        {team.total_points} points
                      </span>
                    </div>
                  )}
                  
                  <div className="mt-auto">
                    <hr />
                    <div className="d-flex justify-content-between align-items-center">
                      <small className="text-muted">
                        <i className="bi bi-calendar-event me-1"></i>
                        {new Date(team.created_at).toLocaleDateString()}
                      </small>
                      <button className="btn btn-sm btn-outline-primary">
                        <i className="bi bi-box-arrow-in-right me-1"></i>
                        Join
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Teams;
