import NavReturn from "./Navbar/Navbar";
import axios from 'axios';

function BackendSend(event)
{
    event.preventDefault();
    var title = document.getElementById("text_title").value;
    var data = document.getElementById("text_data").value;
    alert(title,data);
    var ja = axios.post(
        "http://127.0.0.1:8000/BlogPost/",
        {
            "title" : title,
            "text_data" : data
        },{
            headers:{
                'Content-Type' : "application/json"
            }
        }
    ).then((ersponse)=>{
        console.log(ersponse);
    });
    alert(ja);
}

function AddComponent()
{
    return(
        <div>
            <NavReturn />
            <form onSubmit={BackendSend} method="post">
                <input type="textarea" id="text_title" placeholder="title here" class="input is-rounded" />
                <br/>
                <input type="textarea" id="text_data" placeholder="context here" class="input is-large" />
                <br></br>
                <input type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full rounded shadow" placeholder="send" />
            </form>
        </div>
    )
}
export default AddComponent;