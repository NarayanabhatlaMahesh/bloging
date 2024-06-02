import NavReturn from "./Navbar";
import axios from 'axios';
import { useState, useEffect } from "react";




function Login()
{
    var [b,setb] = useState([]);
    var [valid,setvalid] = useState(false);
    var [usern, setusername] = useState("");
    var [pass, setpassword] = useState("");
    function Verify(event)
    {
        event.preventDefault();
        axios.get("http://127.0.0.1:8000/UsernameGet/",{
            headers:{
                Accept : "application/json",
            },
        }).then(
            Response=>{setb(Response.data);
            }
        ).catch((error)=>{
            console.log(error);
        }); 
        setusername(event.target.usern.value)
        setpassword(event.target.pass.value)  
       
    }

   
    // useEffect( ()=>{
    //     b.forEach(validate);
    // },[b,validate]
    // );
    function validate(index, values)
    {
        setvalid(false)
        if (index.username === usern && index.password === pass)
        {   axios.put("http://127.0.0.1:8000/putlogin/",{
            "log" : "yes"
            },{
                headers:{
                    'Content-Type' : "application/json"
                }
            }).then(
            (res)=>
            {
                console.log(res);
            })
            console.log(valid);
            setvalid(true)
            console.log("set true");
        }
    }
    return(
        <div>
        <NavReturn />
        <div class='centerlogin'>
            <form onSubmit={Verify} method="post">
                <div class="centerlo">
                <input  name="usern" type="text" placeholder="username"  /><br/>
                </div>
                <div class="centerlo">
                <input  name="pass" type="password" placeholder="password" /><br/>
                </div>
                <br/>
                <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full rounded shadow buttoncenter" >send</button>
            </form>
        </div>
        </div>
    );
}

export default Login;