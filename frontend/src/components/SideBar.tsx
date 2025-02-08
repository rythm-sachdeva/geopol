import { useChatStore } from "../store/useChatStore";
import { useEffect } from "react";
import SidebarSkeleton from "./skeletons/SideBarSkeleton";
import { Users } from "lucide-react";
import { useAuthStore } from "../store/useAuthStore";


const SideBar = () => {
    //@ts-ignore
    const {getUsers,users,isUsersLoading,setSelectedUser,selectedUser} = useChatStore();
    const {authUser} = useAuthStore() as any;

    useEffect(()=>{
        getUsers();
    },[getUsers])

    if(isUsersLoading)
    {
        return <SidebarSkeleton/>
    }
    // console.log(authUser)

  return (
   <aside className="h-full w-20 lg:w-72  border-r border-base-200 flex flex-col transition-all duration-200">
    <div className="border-b border-base-300 w-full p-5 ">
      <Users className="size-6" />
      <span className="hidden font-medium lg:block">Contacts</span>

    </div>
    <div className="overflow-y-auto w-full py-3">
        {users.map((user:any) => (
          <button
            key={user.id}
            onClick={() => setSelectedUser(user)}
            className={`
              w-full p-3 flex items-center gap-3
              hover:bg-base-300 transition-colors
              ${authUser?.id === user?.id ? "hidden":"flex"}
              ${selectedUser?.id === user.id ? "bg-base-300 ring-1 ring-base-300" : ""}
            `}
          >
            <div className="relative mx-auto lg:mx-0">
              <img
                src={user.profilePic || "/avatar.png"}
                alt={user.name}
                className="size-12 object-cover rounded-full"
              />
              {/* {onlineUsers.includes(user._id) && (
                <span
                  className="absolute bottom-0 right-0 size-3 bg-green-500 
                  rounded-full ring-2 ring-zinc-900"
                />
              )} */}
            </div>

            {/* User info - only visible on larger screens */}
            <div className="hidden lg:block text-left min-w-0">
              <div className="font-medium truncate">{user.email}</div>
              <div className="text-sm text-zinc-400">
                {/* {onlineUsers.includes(user._id) ? "Online" : "Offline"} */}
              </div>
            </div>
          </button>
        ))}

        {/* {filteredUsers.length === 0 && (
          <div className="text-center text-zinc-500 py-4">No online users</div>
        )} */}
      </div>

   </aside>
  )
}

export default SideBar