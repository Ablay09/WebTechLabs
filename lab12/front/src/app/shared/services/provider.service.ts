import {Injectable, EventEmitter} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { TaskList, TaskShort, Task, TaskNew} from '../models';
import { MainService } from './main.service';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }
  //TaskLists
  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/tasklists/', {});
  }

  createTaskList(name:any): Promise<TaskList> {
    return this.post('http://localhost:8000/api/tasklists/', {
      name:name
    });
  }
  //TaskListDetail
  getTaskListDetail(id: number): Promise<TaskList> {
    return this.get(`http://localhost:8000/api/tasklists/${id}/`, {});
  }

  updateTaskListDetail(taskList: TaskList): Promise<TaskList> {
    return this.put(`http://localhost:8000/api/tasklists/${taskList.id}/`, {
      name: taskList.name
    });
  } 

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasklists/${id}/`, {});
  }

  deleteTaskList2(taskList: TaskList): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasklists/${taskList.id}`, {});
  }

  //TasksOfTaskList
  getTaskListTasks(id: number): Promise<TaskShort[]> {
    return this.get(`http://localhost:8000/api/tasklist/${id}/tasks/`, {});
  } 
  
  createTaskListTasks(taskListId: number, name:string, created_at:string, due_on:string, status: string): Promise<TaskNew> {
    return this.post(`http://localhost:8000/api/tasklist/${taskListId}/tasks/`, {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status
    });
  }
  

  //Tasks - get, put, delete
  getTaskDetail(id: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/tasks/${id}/`, {});
  }

  updateTask(task: Task): Promise<Task> {
    return this.put(`http://localhost:8000/api/tasks/${task.id}/`, {
      name: task.name,
      created_at: task.created_at,
      due_on: task.due_on,
      status: task.status
    });
  } 
  deleteTask(task: Task): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasks/${task.id}/`, {});
  }
}