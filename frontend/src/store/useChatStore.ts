import axios from "axios";
import toast from "react-hot-toast";
import { create } from "zustand";

const useChatStore = create((set)=>({
    messages:[],
    users:[],
    selectedUser:null,
    isUsersLogin:false,
    isMessagesLoading:false,

    getUsers: async ()=>{
      set({isUsersLogin:true});
      try {
        const res = await axios.get(`${import.meta.env.VITE_API_URL}/api/users/`);
        set({users:res.data});

      } catch (error) {
        toast.error("Failed to get users");
      }
      finally{
        set({isUsersLogin:false});
      }

    }
}))