import React from "react";
import { Link } from "react-router-dom";
import Spring from '../Avitar/Spring.png';
import NewNav from "../components/Navbar";

function Home() {
  return (
    <div className="home">

      <img src={require('../Avitar/Spring.png')} style={{
        marginTop: "70px",
        }}/>

    </div>
  );
}

export default Home;
