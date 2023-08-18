import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../img/nav.png';

  const NavBar = () => {

    return (
      <div className='sticky top-0 bg-gray-900 flex justify-between items-center h-24 w-full mx-auto '>
        <div className='w-[1340px] mx-auto bg-gray-900'>
          <Link to="/">
            <img src={logo} alt="logo" ></img>
          </Link>
        </div>
        
      </div>
    );
  }

  export default NavBar;