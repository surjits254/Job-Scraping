import { Component, OnInit} from '@angular/core';
import { FormBuilder, Validators } from "@angular/forms";
 import {JobServiceService} from "./job-service.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'JobScrapping';
  // jobType : any = ['full-time','part-time','contract','others'];

    job : any;
    loc: any;
    jobsOutput :any [];
    public jt: any [];
  checkoutForm = this.fb.group({
    jobType : [''],
    location : ['']
  })

  constructor(public fb: FormBuilder,private myService: JobServiceService) {
    this.myService.arrBirds;
    
    
   }
  onSubmit(value : any) {
    alert(JSON.stringify(this.checkoutForm.value))
    console.log(this.job = this.checkoutForm.value.jobType);
    console.log(this.loc = this.checkoutForm.value.location);
    this.myService.post(this.job,this.loc).subscribe( 
      res => {
        
        //console.log(res['data'][0]['job_type']);
        // let tempArr : any[];

        // this.jt[0] =Response['data'[0]];
        //this.jt = tempArr;
        var jt = new Array();
        for(let pr of res['data']){
          var lst = new Array();
          lst.push(pr.job_title);
          lst.push(pr.job_type);
          console.log(lst);
          jt.push(pr);
          
           //console.log(pr.job_title);
        }
        this.jobsOutput = jt;
        console.log(jt);
        console.log(this.jobsOutput)
      //   this.jobsOutput = res['data'];
      //   let evilResponseProps = Object.keys(this.jobsOutput);
      //   console.log(evilResponseProps);
      //   let goodResp : any [];
      //   for (let prop of evilResponseProps) { 
      //     console.log(evilResponseProps[prop].job_type);
      // }

      // console.log(this.jt);
        // for(let temp of this.jobsOutput){
        //   this.jt = temp;
        //   console.log(typeof temp);
        //   console.log(this.jt);
        // }
        
       // console.log(this.jobsOutput['data'][0].job_type);
          // this.arrBirds = res['data'][0]['job_type'];	 // FILL THE ARRAY WITH DATA.
          //   console.log(this.arrBirds);
          //   return this.arrBirds;
        },
        
      );;

    // this.myService.post.

    // res =>

  }

  
}
