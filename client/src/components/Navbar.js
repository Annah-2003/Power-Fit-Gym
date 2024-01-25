import React from 'react'
import { Link } from 'react-router-dom'

function NewNav() {
  return (
    <nav>
        <ul>
            <div className='logo'>
                <img src={require('../Avitar/Spring.png')} width={'40px'} />
            </div>
            <div className='menu-items'> 
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                {/* <li><Link to="/enrolled">Enrolled</Link></li> */}
                <li><Link to="/register">Register</Link></li>
                <li><Link to="/enrolled">Admin</Link></li>
                <li><Link to="/about">Click Me!</Link></li>
            </div>
            
        </ul>
    </nav>
  )
}

export default NewNav