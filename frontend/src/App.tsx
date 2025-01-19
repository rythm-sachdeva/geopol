import './App.css'
import Navbar from './components/Navbar'
import { Routes,Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import SignupPage from './pages/SignupPage'
import SettingsPage from './pages/SettingsPage'
import ProfilePage from './pages/ProfilePage'
import { Toaster } from 'react-hot-toast'

function App() {
  return (
    <div className=''>
     <Navbar/>
     <div className='md:pt-7'>
     <Routes>
       <Route path="/" element={<HomePage/>} />
       <Route path="/login" element={<LoginPage/>}/>
       <Route path="/signup" element={<SignupPage/>} /> 
       <Route path="/settings" element={<SettingsPage/>} />
       <Route path="/profile" element={<ProfilePage/>} />
     </Routes>
     </div>
    <Toaster/>
    </div>
  )
}

export default App
