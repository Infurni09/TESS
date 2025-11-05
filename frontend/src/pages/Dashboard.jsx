import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Doughnut } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(ArcElement, Tooltip, Legend);

export default function Dashboard(){
  const [data, setData] = useState(null);

  useEffect(()=>{
    async function load(){
      try{
        // For demo: ask backend for per-topic mastery - here we query mastery table via a new endpoint or fetch all mastery rows
        const res = await axios.get('http://localhost:8000/api/events/list');
        // demo: if no backend-specific mastery API, we show placeholder
        setData({
          labels: ['Addition','Subtraction','Multiplication','Division'],
          datasets: [{
            label: 'Mastery',
            data: [0.75,0.6,0.4,0.9],
            backgroundColor: ['#4caf50','#2196f3','#ff9800','#e91e63'],
            hoverOffset: 4
          }]
        });
      }catch(e){
        console.error(e)
      }
    }
    load()
  },[])

  return (
    <div style={{padding:24}}>
      <h2>Mastery Dashboard</h2>
      <p>Donut chart shows per-topic mastery (0..1). Once you run diagnostics the backend will update real values.</p>
      {data ? <div style={{width:360}}><Doughnut data={data} /></div> : <p>Loading...</p>}
    </div>
  );
}

