import { Route, Routes } from "react-router-dom";
import Home from "../pages/Home";
import About from '../pages/About';
import Register from "../pages/Register";
import Navbar from "./Navbar"; 
import Display from './Display';
import Enrolled from "../pages/Enrolled";
import './App.css'
import NewNav from "./Navbar";

function App() {

  return (
    <>
      <div className="App">
        <NewNav />

        <div className="body">
        <Routes>
            <Route path="/about" element={ <About/> } />
            <Route path="/enrolled" element={ <Enrolled/> } />
            <Route path="/register" element={ <Register/> } />
            <Route path="/users/:id" element={ <Display/>} />
            <Route path="/" element = { <Home/> } />
        </Routes>
        </div>
      
      </div>
    </>
      
  );
}

export default App;