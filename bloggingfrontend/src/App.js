import axios from 'axios';
import NavReturn from './Navbar/Navbar';
import {useEffect, useState} from 'react';

function App()
{
  const [a,Seta]=useState([])
  useEffect(()=>{axios.get("http://127.0.0.1:8000/BlogGet/").then(
    Response=>{console.log(Response.data);
      Seta(Response.data);
    }
  ).catch((error)=>{
    console.log(error);
  })},[]);


  return (
    <div>
     <NavReturn />
     <div >
    {
     a.map((Info)=>{ 
      return(
        <div class="center">
        <p><b>Blog title is = {Info.title}</b></p>
        <p> {Info.text_data}</p>
        <hr/>
        </div>
        );
      })
    }
    </div>
      </div>
   );
}

export default App;