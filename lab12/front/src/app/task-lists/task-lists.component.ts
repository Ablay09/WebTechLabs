import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { TaskList } from '../shared/models';
import { Location } from '@angular/common';

@Component({
  selector: 'app-task-lists',
  templateUrl: './task-lists.component.html',
  styleUrls: ['./task-lists.component.sass']
})
export class TaskListsComponent implements OnInit {
  public name: string = '';
  public taskLists: TaskList[] = [];


  constructor(
    private provider: ProviderService,
    private location: Location
    ) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }

  createTaskList() {
    if (this.name != '') {
      this.provider.createTaskList(this.name).then(res => {
        this.taskLists.push(res);
      });
    }
  }

  navigateBack(){
    this.location.back()
  }
}