import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function About() {
  const [instructors, setInstructors] = useState([{}]);
  const [index, setIndex] = useState(0);

  useEffect(() => {
    fetch('/instructors')
      .then((r) => r.json())
      .then((r) => setInstructors(r));

  }, []);

  const results = instructors.map((instructor) => instructor);
  const containPrev = index > 0;
  const containNext = index < results.length - 1;

  function handlePrevClick() {
    if (containPrev) {
      return setIndex(index - 1);
    }
  }

  function handleNextClick() {
    if (containNext) {
      return setIndex(index + 1);
    }
    if (index === results.length - 1);
    return setIndex(0);
  }

  const result = results[index];

  return (
    <div>
      <h1 className="text-primary">Our Instructors</h1>

      <section className="user_container">
        <div key={result.id} className="card bg-light p-3">
          <h3>({index + 1} of {results.length})</h3>
          <h2 className="bg-info text-white p-2 rounded">{result.name}</h2>
          <h5>Gender: {result.gender}</h5>
          <h5>Level: {result.level}</h5>
          <div className="d-flex justify-content-between">
            <button className="btn btn-primary" onClick={handlePrevClick}>
              Previous
            </button>
            <button className="btn btn-primary" onClick={handleNextClick}>
              Next
            </button>
          </div>
          <p>
            <Link to="/register">
              <button className="btn btn-success">Click here to Register</button>
            </Link>
          </p>
        </div>
      </section>
    </div>
  );
}

export default About;
