import { create } from "zustand";

export const useAuthStore = create(
    (set)=>(
        {
            authUser: null,
            isLogginIn:false,
            isSigningUp:false,
            

            isCheckingAuth: true,
            changeCheckingAuth : ()=>set((state:any)=>({isCheckingAuth:!state}))
        }
    )
)