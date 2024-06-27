import { useEffect, useState } from "react";
import Navbar from "./Navbar/Navbar";
import axios from "axios";
import 

function HomePage()
{

    const [data, setdata]=useState([]);
    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/blog/BlogGet/").then(
            Response => {
                setdata(Response.data);
                console.log(localStorage.getItem('key'));
                console.log();
            }
        ).catch((error) =>
            {
                console.log(error);
            }
        )
    },[]);

    return(
        <div>
            <Navbar />
            {
                data.map((info)=>{
                    return(
                        <div>
                            <p>
                                title is :{info.title}
                            </p>
                            <p> data is {info.text_data}</p>
                            <br />
                            <br />
                        </div>
                    )
                })
            }
        </div>
    )
}

export default HomePage;