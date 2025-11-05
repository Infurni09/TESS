import React, {useState,useEffect} from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Event from './pages/Event'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Nav from './components/Nav'
import './styles.css'

function App(){
  const [isAdmin, setIsAdmin] = useState(false)

  useEffect(()=>{
    try {
      const t = localStorage.getItem('token')
      if (t) {
        // decode token payload to check admin flag without verifying (demo only)
        const payload = JSON.parse(atob(t.split('.')[1]))
        setIsAdmin(Boolean(payload.is_admin || payload.isAdmin || payload.is_admin))
      }
    } catch(e){}
  },[])

  return (
    <BrowserRouter>
      <Nav isAdmin={isAdmin}/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login onLogin={(admin)=>setIsAdmin(admin)}/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/event/:id' element={<Event/>}/>
      </Routes>
    </BrowserRouter>
  )
}
createRoot(document.getElementById('root')).render(<App />)
