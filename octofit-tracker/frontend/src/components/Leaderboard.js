import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Helper function to get avatar URL from username
  const getAvatarUrl = (username) => {
    return `/avatars/${username}.svg`;
  };

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard - Fetching from API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard - Processed data:', leaderboardData);
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Leaderboard - Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading leaderboard...</p>
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
          <i className="bi bi-trophy-fill me-2"></i>
          Leaderboard
        </h2>
        <span className="badge bg-warning text-dark">{leaderboard.length} Competitors</span>
      </div>
      
      {leaderboard.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle-fill me-2"></i>
          No leaderboard data available yet. Start tracking activities to compete!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead>
              <tr>
                <th><i className="bi bi-hash me-1"></i>Rank</th>
                <th><i className="bi bi-image me-1"></i>Avatar</th>
                <th><i className="bi bi-person me-1"></i>User</th>
                <th><i className="bi bi-fire me-1"></i>Total Calories</th>
                <th><i className="bi bi-list-ol me-1"></i>Activities</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, index) => {
                let rankBadgeClass = 'bg-secondary';
                let rankIcon = '';
                const username = entry.user || entry.username;
                
                if (index === 0) {
                  rankBadgeClass = 'bg-warning text-dark';
                  rankIcon = '🥇 ';
                } else if (index === 1) {
                  rankBadgeClass = 'bg-light text-dark';
                  rankIcon = '🥈 ';
                } else if (index === 2) {
                  rankBadgeClass = 'bg-bronze text-white';
                  rankIcon = '🥉 ';
                }
                
                return (
                  <tr key={entry.id || index}>
                    <td>
                      <span className={`badge ${rankBadgeClass} fs-6`}>
                        {rankIcon}{index + 1}
                      </span>
                    </td>
                    <td>
                      <img 
                        src={getAvatarUrl(username)} 
                        alt={username}
                        className="avatar-img-small"
                        onError={(e) => { e.target.style.display = 'none'; }}
                      />
                    </td>
                    <td><strong>{username}</strong></td>
                    <td>
                      <strong className="text-danger">
                        <i className="bi bi-fire me-1"></i>
                        {entry.total_calories}
                      </strong>
                    </td>
                    <td>
                      <span className="badge bg-primary rounded-pill">{entry.activities_count}</span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
