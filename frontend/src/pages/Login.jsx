import React,{useState} from 'react';
import axios from 'axios';
export default function Login({ onLogin }){
  const [identifier,setIdentifier]=useState(''); // username or email
  const [password,setPassword]=useState('');
  async function doLogin(){
    try{
      const res = await axios.post('http://localhost:8000/api/auth/login',{
        identifier: identifier,
        password: password
      });
      const token = res.data.access_token || res.data.token;
      localStorage.setItem('token', token);
      const isAdmin = res.data.is_admin || (res.data && res.data.is_admin) || false;
      if (onLogin) onLogin(Boolean(isAdmin));
      alert('Logged in');
    }catch(e){
      console.error(e)
      alert('Login failed');
    }
  }
  return (
    <div style={{padding:24}}>
      <h2>Login</h2>
      <input placeholder='username or email' value={identifier} onChange={e=>setIdentifier(e.target.value)} /><br/>
      <input type='password' placeholder='password' value={password} onChange={e=>setPassword(e.target.value)} /><br/>
      <button onClick={doLogin}>Login</button>
    </div>
  )
}
