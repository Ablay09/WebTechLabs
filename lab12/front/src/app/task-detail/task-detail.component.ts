import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Task, TaskNew, TaskShort} from '../shared/models';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.sass']
})
export class TaskDetailComponent implements OnInit {

  public id: number = 0;

  public task: any = {}

  public taskName: string ="";
  public task_created_at: any = new Date().toISOString();
  public task_due_on: any;
  public taskStatus: string = "";
  

  constructor(
    private provider: ProviderService,
    private route: ActivatedRoute,
    private location: Location
  ) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'))

    if(this.id){
      this.provider.getTaskDetail(this.id).then(res => {
        this.task = res
      })
    }
  }

  updateTask(task: Task) {
    this.provider.updateTask(task).then(res => {
      console.log(task + ' updated');
    });
  }

  deleteTask(task:Task){
    this.provider.deleteTask(task).then(() => {
      console.log(task + ' deleted');
    });
  }

  navigateBack(){
    this.location.back()
  }
}
