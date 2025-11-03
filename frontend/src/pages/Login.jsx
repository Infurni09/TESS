import React,{useState} from 'react';
import axios from 'axios';
export default function Login(){
  const [email,setEmail]=useState('');
  const [password,setPassword]=useState('');
  async function doLogin(){
    try{
      const res = await axios.post('http://localhost:8000/api/auth/login',{email,password});
      localStorage.setItem('token', res.data.access_token || res.data.token);
      alert('Logged in');
    }catch(e){
      alert('Login failed');
    }
  }
  return (
    <div style={{padding:24}}>
      <h2>Login</h2>
      <input placeholder='email' value={email} onChange={e=>setEmail(e.target.value)}/><br/>
      <input type='password' placeholder='password' value={password} onChange={e=>setPassword(e.target.value)}/><br/>
      <button onClick={doLogin}>Login</button>
    </div>
  );
}
