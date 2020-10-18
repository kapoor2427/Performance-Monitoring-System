import React,{Component} from 'react';
import {NavLink} from 'react-router-dom'
import CommonNavbar from './Navbar';

class Top extends Component {

	state={
   posts:[],
   processes:[]
}

componentDidMount(){
   this.getdata();
   this.interval=setInterval(() => {
      this.getdata();
   }, 5000);


}

componentWillUnmount () {
   
   clearInterval(this.interval);
 }




getdata=() =>{
   var xhr = new XMLHttpRequest();
//var data = null
xhr.withCredentials = true;

xhr.onload= function (e){
   if(xhr.readyState===4){
      if(xhr.status===200){
         this.setState({
            posts:JSON.parse(xhr.response)["data"],
            maxCores:JSON.parse(xhr.response)["maxCores"]
         })
      }
   }
}.bind(this);


    xhr.open("GET","http://127.0.0.1:5000/api/data");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("cache-control", "no-cache");
xhr.setRequestHeader("Postman-Token", "96de2df0-0da1-4bf1-be8a-1f4ffab9de85");

xhr.send();

}


render() {

   const { posts} = this.state;
   const postList = posts.length ? (
      posts.map(post=>{
         var i=0;
         return(
            <>
            <tr>
               <td key={post.macAddress}>{post.macAddress}</td>
               <td>
                 <li><span className="Left"><b>{post.topMemoryUsingProcesses[i].name}:</b></span><span className="Right"> {post.topMemoryUsingProcesses[i].memory_percent + ' %'}</span></li>
                <li ><span className="Left"><b>{post.topMemoryUsingProcesses[i+1].name}:</b></span> <span className="Right"> {post.topMemoryUsingProcesses[i+1].memory_percent + ' %'}</span></li>
                <li><span className="Left"><b>{post.topMemoryUsingProcesses[i+2].name}:</b></span> <span className="Right"> {post.topMemoryUsingProcesses[i+2].memory_percent + ' %'}</span></li>
                <li><span className="Left"><b>{post.topMemoryUsingProcesses[i+3].name}:</b></span> <span className="Right"> {post.topMemoryUsingProcesses[i+3].memory_percent + ' %'}</span></li>
                <li><span className="Left"><b>{post.topMemoryUsingProcesses[i+4].name}:</b></span> <span className="Right">{post.topMemoryUsingProcesses[i+4].memory_percent + ' %'}</span></li>
               </td>
               <td>
                  <li><span className="Left"><b>{post.topCPUUsingProcesses[i].name}:</b></span><span className="Right"> {post.topCPUUsingProcesses[i].cpu_percent + ' %'}</span></li>
                  <li><span className="Left"><b>{post.topCPUUsingProcesses[i+1].name}:</b></span><span className="Right"> {post.topCPUUsingProcesses[i+1].cpu_percent + ' %'}</span></li>
                  <li><span className="Left"><b>{post.topCPUUsingProcesses[i+2].name}:</b></span><span className="Right"> {post.topCPUUsingProcesses[i+2].cpu_percent + ' %'}</span></li>
                  <li><span className="Left"><b>{post.topCPUUsingProcesses[i+3].name}:</b></span><span className="Right"> {post.topCPUUsingProcesses[i+3].cpu_percent + ' %'}</span></li>
                  <li><span className="Left"><b>{post.topCPUUsingProcesses[i+4].name}:</b></span><span className="Right"> {post.topCPUUsingProcesses[i+4].cpu_percent + ' %'}</span></li>
               </td> 
               </tr>
</>
         )
      })
   ) : (
      <div className="text-center">
      <div className="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>
   )

   return (
     <div>
        <CommonNavbar/> 
    <div className="container">                   
                <table class="table table-hover" style={{width:"100%", marginTop:"10%", textAlign:"center"}}>
                    <thead>
                        <tr id='students' >
                  <th>Mac Address</th>
                  <th>Top 5 Memory Using Processes</th>
                  <th>Top 5 CPU Using Processes</th>
               </tr>
               </thead>
               {postList}                    
                </table>            
                
   </div> 
     </div>
  )
}
}

export default Top;

