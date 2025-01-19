import axios from "axios";
import toast from "react-hot-toast";
import { create } from "zustand";
import { LoginResponse } from "../lib/types";

export const useAuthStore = create(
    (set)=>(
        {
            authUser: null,
            isLogginIn:false,
            isSigningUp:false,
            logout:false,


            isCheckingAuth: true,
            changeCheckingAuth : ()=>set((state:any)=>({isCheckingAuth:!state})),
            loginFunc: async(data:any)=>{
                set({isLogginIn:true})
                try {
                  if(data.email && data.password)
                  {
                    const res : any = await axios.post(`${import.meta.env.VITE_API_URL}/accounts/login/`,data)
                  set({authUser:res.data?.user})
                  console.log(res.data.token)
                  localStorage.setItem("token",res.data?.token)
                  toast.success("Logged In Successfully")
                  }
                  else{
                    toast.error("Email or Password Cannot be blank")
                  }
                    
                } catch (error) {
                    console.log(error)
                     if(axios.isAxiosError(error))
                         {

                            toast.error("Invalid Email or Password")
                         }
                         else
                         {
                            toast.error("An Unexpected Error Occured")
                         }
                } finally{
                    set({isLogginIn:false})
                }
            }
        }
    )
)