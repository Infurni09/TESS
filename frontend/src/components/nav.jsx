import React from 'react';
import { Link } from 'react-router-dom';

export default function Nav({ isAdmin }) {
  return (
    <div className="topbar">
      <div style={{display:'flex', gap:12, alignItems:'center'}}>
        <Link to="/" style={{color:'#fff', fontWeight:700, textDecoration:'none'}}>TESS</Link>
        <Link to="/" style={{color:'#fff', textDecoration:'none'}}>Home</Link>
        <Link to="/dashboard" style={{color:'#fff', textDecoration:'none'}}>Dashboard</Link>
      </div>
      <div>
        {isAdmin && <Link to="/admin" style={{color:'#fff', marginRight:12}}>Admin</Link>}
        <Link to="/login" style={{color:'#fff'}}>Login</Link>
      </div>
    </div>
  );
}
