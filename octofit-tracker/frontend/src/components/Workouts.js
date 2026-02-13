import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts - Fetching from API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts - Raw API response:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Workouts - Error fetching data:', error);
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
        <p className="mt-3 text-muted">Loading workouts...</p>
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

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      'Beginner': 'success',
      'Intermediate': 'warning',
      'Advanced': 'danger'
    };
    return badges[difficulty] || 'secondary';
  };

  return (
    <div className="container mt-4">
      <div className="page-header">
        <h2>
          <i className="bi bi-lightning-charge-fill me-2"></i>
          Workout Suggestions
        </h2>
        <span className="badge bg-success">{workouts.length} Workouts</span>
      </div>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          <i className="bi bi-info-circle-fill me-2"></i>
          No workout suggestions available at the moment.
        </div>
      ) : (
        <div className="row g-4">
          {workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <div className="d-flex justify-content-between align-items-start mb-2">
                    <h5 className="card-title">
                      <i className="bi bi-lightning me-2 text-warning"></i>
                      {workout.name}
                    </h5>
                    <span className={`badge bg-${getDifficultyBadge(workout.difficulty)}`}>
                      {workout.difficulty}
                    </span>
                  </div>
                  <p className="card-text flex-grow-1">{workout.description}</p>
                  <div className="mt-auto">
                    <hr />
                    <div className="d-flex justify-content-between mb-2">
                      <span className="badge bg-light text-dark">
                        <i className="bi bi-clock me-1"></i>
                        {workout.duration_minutes} min
                      </span>
                      <span className="badge bg-light text-dark">
                        <i className="bi bi-tag me-1"></i>
                        {workout.category}
                      </span>
                    </div>
                    <button className="btn btn-primary w-100">
                      <i className="bi bi-play-circle me-1"></i>
                      Start Workout
                    </button>
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

export default Workouts;
