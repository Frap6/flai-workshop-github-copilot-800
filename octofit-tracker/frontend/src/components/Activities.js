import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Activities - Fetching from API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        console.log('Activities - Processed data:', activitiesData);
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Activities - Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading activities...</p>
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
          <i className="bi bi-activity me-2"></i>
          Activities
        </h2>
        <span className="badge bg-primary">{activities.length} Total</span>
      </div>
      
      {activities.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle-fill me-2"></i>
          No activities found. Start logging your workouts!
        </div>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead>
              <tr>
                <th><i className="bi bi-tag me-1"></i>Activity Type</th>
                <th><i className="bi bi-clock me-1"></i>Duration (min)</th>
                <th><i className="bi bi-fire me-1"></i>Calories</th>
                <th><i className="bi bi-calendar me-1"></i>Date</th>
                <th><i className="bi bi-person me-1"></i>User</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity) => (
                <tr key={activity.id}>
                  <td>
                    <span className="badge bg-secondary">{activity.activity_type}</span>
                  </td>
                  <td><strong>{activity.duration_minutes}</strong></td>
                  <td><strong className="text-danger">{activity.calories_burned}</strong></td>
                  <td>{new Date(activity.date).toLocaleDateString()}</td>
                  <td>{activity.user}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Activities;
