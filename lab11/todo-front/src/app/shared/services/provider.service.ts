import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { TaskList, TaskShort, Task } from '../models';
import { MainService } from './main.service';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  // public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/tasklists/', {});
  }
  

  getTaskListDetail(id: number): Promise<TaskList> {
    return this.get(`http://localhost:8000/api/tasklists/${id}/`, {});
  }

  getTaskListTasks(id: number): Promise<TaskShort[]> {
    return this.get(`http://localhost:8000/api/tasklist/${id}/tasks/`, {});
  }

  getTaskDetail(id: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/tasks/${id}/`, {});
  }

}