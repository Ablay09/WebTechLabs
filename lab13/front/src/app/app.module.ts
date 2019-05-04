import { BrowserModule } from '@angular/platform-browser';
import { NgModule, ClassProvider } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { TaskListsComponent } from './task-lists/task-lists.component';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { TaskListTasksComponent } from './task-list-tasks/task-list-tasks.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { ProviderService } from './shared/services/provider.service';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BaseComponent } from './base/base.component';
import { AuthInterceptor } from './AuthInterceptor';
import { AuthComponent } from './auth/auth.component';
import { LogoutComponent } from './logout/logout.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskListsComponent,
    TaskListDetailComponent,
    TaskListTasksComponent,
    TaskDetailComponent,
    BaseComponent,
    AuthComponent,
    LogoutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
