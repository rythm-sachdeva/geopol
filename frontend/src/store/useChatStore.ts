import { create } from "zustand";

const useChatStore = create((set)=>({
    messages:[],
    users:[],
    selectedUser:null,
    isUsersLogin:false,
    isMessagesLoading:false,

    getUsers: async ()=>{
      set({isUsersLogin:true})
    }
}))