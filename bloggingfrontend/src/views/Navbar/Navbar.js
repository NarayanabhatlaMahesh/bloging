import { Link } from "react-router-dom";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";




function NavReturn()
{
  var navigate = useNavigate();
  const location = useLocation();
  console.log('auth key is ========',localStorage.getItem('Auth_key'));
  const [key,setkey] = useState(localStorage.getItem('Auth_key'));

  function redirectLogin()
  {
    
    
    const currentUrl = location.pathname;
    console.log('key is -->',currentUrl);
    if(key=='null')navigate('/login')
    else
    {
      console.log('key is  ',localStorage.getItem('Auth_key'));
      localStorage.setItem('Auth_key',null);
      if(currentUrl=='/')
        window.location.reload();

      else  navigate('/');
    
    }
  }
    
  
    return(
  <nav>
    
    <div class="nav-wrapper">
      <Link to="/" class="brand-logo">BLOG</Link>
      
      <ul class="right hide-on-med-and-down">
          
          <li>
            <a onClick={redirectLogin}><i  class="material-icons right">{key=='null'?'login':'logout'}</i></a>
          </li>
          <li>
            <Link to="/WriteBlog"><i class="material-icons right">edit_document</i></Link>
          </li>
      </ul>
      <ul class="input-field right">
            <li>
            <input type="search" placeholder="search" />
            </li>
      </ul>
    </div>
  </nav>
);
}

export default NavReturn;