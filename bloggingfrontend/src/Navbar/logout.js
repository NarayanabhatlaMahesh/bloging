import { useState } from "react";
import axios from "axios";

function Logout()
{
    const [log,setlog] = useState("");
    axios.put("http://127.0.0.1:8000/putlogin/",{
            "log" : "no"
            },{
                headers:{
                    'Content-Type' : "application/json"
                }
            }).then(
            (res)=>
            {
                console.log(res);
                setlog("no");
            })
        
            return(
                <div>
                    <p>{log==="no"?'logged out':'still logged in'}</p>
                </div>    
            )
}

export default Logout;