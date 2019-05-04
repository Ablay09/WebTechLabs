export interface User{
    id: number,
    username: string,
    email: string
}

export interface TaskList {
    id: number,
    name: string,
    owner: User
}

export interface TaskShort {
    id: number,
    name: string,
    status: string
}

export interface Task {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string
}

export interface TaskNew {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string,
    task_list: TaskList
}

export interface AuthResponse {
    token: string;
}

