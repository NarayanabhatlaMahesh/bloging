import axios from 'axios';

function LoginEvent(event) {
    var Resp;
    return axios.post("http://127.0.0.1:8000/api-token-auth/", {
        'username': event.target.usern.value,
        'password': event.target.pass.value
    }, {
        headers: {
            Accept: "application/json",
        }
    })
}

export default LoginEvent;