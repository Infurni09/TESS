import React,{useState} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
const API='http://localhost:8000';
export default function Event(){
  const { id } = useParams();
  const [q,setQ]=useState(null);
  async function start(which){
    try{
      const res = await axios.post(`${API}/api/sessions/start/1/${encodeURIComponent(id)}?mode=diagnostic&which=${which}`);
      setQ(res.data.question);
    }catch(e){ console.error(e); alert('Error starting session'); }
  }
  async function submit(choice){
    if(!q) return;
    try{
      const res = await axios.post(`${API}/api/sessions/submit/1`, null, { params: { user_id:1, event_id:id, question_id: q.id, selected: choice } });
      alert('Correct: '+res.data.correct + '\\nMastery: '+(res.data.new_mastery||0).toFixed(2));
      setQ(null);
    }catch(e){ console.error(e); alert('Submit error'); }
  }
  return (
    <div className='content'>
      <h2>{id}</h2>
      <div className='card'>
        <button onClick={()=>start(1)}>Start D1</button>
        <button onClick={()=>start(2)}>D2</button>
        <button onClick={()=>start(3)}>D3</button>
        <button onClick={()=>start(null)}>Practice</button>
      </div>
      {q && <div className='card'>
        <div>{q.question}</div>
        {q.choices.map((c,i)=>(<div key={i} className='choice' onClick={()=>submit(c)}>{c}</div>))}
      </div>}
    </div>
  );
}
