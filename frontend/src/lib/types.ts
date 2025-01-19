export interface signupForm{
    fullName:string,
    email : string,
    password:string
}

export interface loginForm{
    email : string,
    password:string
}

interface User {
    email: string;
    id: string;
  }
  
export interface LoginResponse {
    message: string;
    token: string;
    user: User;
  }