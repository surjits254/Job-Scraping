import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class JobServiceService {
  readonly ROOT_URL;
  

   post$: Observable<any>;
    private myMethodSubject = new Subject<any>();

    constructor(private http: HttpClient) {
      this.ROOT_URL = "http://3.89.160.252:5000/search";
        this.post$ = this.myMethodSubject.asObservable();
    }
    arrBirds: string [];
    post(job_type : any, location : any) {
        console.log(job_type);
        console.log(location); 
        
        
         this.http.post(`${this.ROOT_URL}`,job_type,location);
         return this.http.post(`${this.ROOT_URL}`,{job_type,location});
        // .subscribe(
        //   res => {

        //   //console.log(res['data'][0]['job_type']);
          
          
        //     this.arrBirds = res['data'][0]['job_type'];	 // FILL THE ARRAY WITH DATA.
        //       console.log(this.arrBirds);
        //       return this.arrBirds;
        //   },
          
        // );
    }
}
