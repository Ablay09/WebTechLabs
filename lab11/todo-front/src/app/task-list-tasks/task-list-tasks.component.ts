import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { Task, TaskShort, TaskList } from '../shared/models';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-task-list-tasks',
  templateUrl: './task-list-tasks.component.html',
  styleUrls: ['./task-list-tasks.component.sass']
})
export class TaskListTasksComponent implements OnInit {

  public tasks: TaskShort[] = [];
  public taskList: any = {};

  public id: number;

  constructor(
    private provider: ProviderService,
    private route: ActivatedRoute,
    private location: Location
    ) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'))
    if(this.id){
      this.provider.getTaskListTasks(this.id).then(res => {
        this.tasks = res
      })
      this.provider.getTaskListDetail(this.id).then(res => {
        this.taskList = res
      })
    }
  }

  navigateBack(){
    this.location.back()
  }

}
