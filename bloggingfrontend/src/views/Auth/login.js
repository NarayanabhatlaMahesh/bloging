import NavReturn from "../Navbar/Navbar";
import axios from 'axios';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Snackbar from '@mui/material/Snackbar';
import LoginEvent from "../Auth/AuthService/loginservice";




function Login() {
    const navigate = useNavigate();

    function Verify(event) {
        if(!event.target.usern.value && !event.target.pass.value)
        {
            event.preventDefault();
            setmessage("Please Fill All Values");
            handleClick();
        }
        else
        {
            console.log('in verify after filling values')
            event.preventDefault();
            // console.log('loginevent response is ====',);
            LoginEvent(event).then(
                Response => {
                    console.log('returning ',Response)
                    localStorage.setItem('Auth_key', Response.data['token']);
                    navigate('/');
                    
                }
            ).catch((error) => {
                console.log('ERROR is ===',error);
                setmessage("Login Failed");
                handleClick();
            });

            

            
        }
    }
    
    const [message, setmessage] = React.useState("");
    const [state, setState] = React.useState({
        open: false,
        vertical: 'top',
        horizontal: 'center'
      });
      const { vertical, horizontal, open } = state;
    
      const handleClick  = () => {
        setState({ vertical: 'top',
                    horizontal: 'center',
                    open: true });
      };
    
      const handleClose = () => {
        setState({ ...state, open: false });
      };
    return (
        <div>
            <NavReturn />
            <div class='centerlogin'>
                <form onSubmit={Verify}>
                    <div class="centerlo">
                        <input name="usern" type="text" placeholder="username" /><br />
                    </div>
                    <div class="centerlo">
                        <input name="pass" type="password" placeholder="password" /><br />
                    </div>
                    <br />
                    <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full rounded shadow buttoncenter" >Login</button>
                </form>
            </div>
            <div>
                <Snackbar
                    open={open}
                    autoHideDuration={4000}
                    anchorOrigin={{ vertical, horizontal }}
                    onClose={handleClose}
                    message={message}
                    key={vertical + horizontal}
                />
            </div>
        </div>
    );
}

export default Login;