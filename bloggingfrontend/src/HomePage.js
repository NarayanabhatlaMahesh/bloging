import { useEffect, useState } from "react";
import Navbar from "./Navbar/Navbar";
import axios from "axios";

function HomePage()
{

    const [data, setdata]=useState([]);
    useEffect(()=>{
        axios.get("http://127.0.0.1:8000/BlogGet/").then(
            Response => {
                setdata(Response.data);
                console.log(data);
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
                            <p> ata is {info.text_data}</p>
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