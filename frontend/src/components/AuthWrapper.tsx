import React, { useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/useAuthStore';

const AuthWrapper = ({children}:{children:React.ReactNode}) => {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();
   const changeCheckingAuth = useAuthStore((state:any)=>state.isCheckingAuth)
   useEffect(()=>{
    if(!token)
         {
            navigate('/login')
         }
        else{
           changeCheckingAuth()
        }
  },[])


  return (
    <>
    {children}
    </>
  )
}

export default AuthWrapper