import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TaskListsComponent } from './task-lists/task-lists.component';
import { AppComponent } from './app.component';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { TaskListTasksComponent } from './task-list-tasks/task-list-tasks.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { BaseComponent } from './base/base.component';
import { AuthComponent } from './auth/auth.component';
import { LogoutComponent} from './logout/logout.component';

const routes: Routes = [
  {path: '', component: BaseComponent},
  {path: 'tasklists', component: TaskListsComponent},
  {path: 'tasklists/:id', component: TaskListDetailComponent},
  {path: 'tasklist/:id/tasks', component: TaskListTasksComponent},
  {path: 'tasks/:id', component: TaskDetailComponent},
  {path: 'login', component: AuthComponent},
  {path: 'logout', component: LogoutComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
