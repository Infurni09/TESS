import React from 'react';
import { Link } from 'react-router-dom';
const EVENTS = ['Business Services','Finance','Hospitality & Tourism','Marketing','Principles of Business Management','Principles of Finance','Principles of Hospitality & Tourism','Principles of Marketing'];
export default function Home(){
  return (
    <div className='content'>
      <h1>TESS</h1>
      {EVENTS.map((e,i)=>(
        <div key={i} className='card'>
          <h3>{e}</h3>
          <Link to={'/event/'+encodeURIComponent(e)}>Open</Link>
        </div>
      ))}
    </div>
  );
}
