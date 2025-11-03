import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Event from './pages/Event'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import './styles.css'

function App(){
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/login' element={<Login/>}/>
        <Route path='/dashboard' element={<Dashboard/>}/>
        <Route path='/event/:id' element={<Event/>}/>
      </Routes>
    </BrowserRouter>
  )
}
createRoot(document.getElementById('root')).render(<App />)
