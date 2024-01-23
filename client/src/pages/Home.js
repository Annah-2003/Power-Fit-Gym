import React from "react";
import { Link } from "react-router-dom";
import Spring from '../Avitar/Spring.jpg.png';

function Home() {
  return (
    <>
      <div className="button-container">
        <h3>
          <Link to="/enrolled"><button type="admin">ADMIN</button></Link>
        </h3>
        <h2>
          <Link to="/about"><button>Click Me!</button></Link>
        </h2>
      </div>
      <section>
        <img src={Spring} className="Spring" alt="exercise" />
      </section>
    </>
  );
}

export default Home;
