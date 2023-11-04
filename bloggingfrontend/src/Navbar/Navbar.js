import { Link } from "react-router-dom";
import axios from "axios";
import { useEffect, useState } from "react";



function NavReturn()
{
  const [log,setlog] = useState("");
  useEffect(function loginin()
  {
    axios.get("http://127.0.0.1:8000/getLogin/").then(
    Response=> {
        setlog(Response.data[0].login)
    })
  },[])
  
    return(
  <nav>
    
    <div class="nav-wrapper">
      <Link to="/" class="brand-logo">BLOG</Link>
      
      <ul class="right hide-on-med-and-down">
          
          <li>
            <Link to="/login"><i class="material-icons right">{{log}?'login':'logout'}</i></Link>
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