import React,{Component} from 'react';
import {NavLink} from 'react-router-dom'
import CommonNavbar from './Navbar';


class Table extends Component {


    state={
   posts:[]
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
         return(
            <tbody id="students" key={post.macAddress} >
                <td>{post.macAddress}</td>
                <td>{post.cpuUsage.Core0 + ' %'}</td>
                <td>{post.cpuUsage.Core1 + ' %'}</td>
                <td>{post.cpuUsage.Core2 + ' %'}</td>
                <td>{post.cpuUsage.Core3 + ' %'}</td>
                <td>{post.cpuUsage.Core4 + ' %'}</td>
                <td>{post.cpuUsage.Core5 + ' %'}</td>
                <td>{post.memoryUsage + ' %'}</td>
                <td>{post.diskUsage + ' %'}</td>
            </tbody>

         )
      })
   ) :  (
      <div className="text-center">
      <div className="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
      </div>
   )
   console.log({postList});

  return (
     <div>
     <CommonNavbar/>
     <div className="container">                   
                <table class="table table-hover" style={{width:"100%", marginTop:"10%", textAlign:"center"}}>
                    <thead>
                        <tr id='students' >
                  <th>Mac Address</th>
                  <th>Cpu CORE1</th>
                  <th>Cpu CORE2</th>
                  <th>Cpu CORE3</th>
                  <th>Cpu CORE4</th>
                  <th>Cpu CORE5</th>
                  <th>Cpu CORE6</th>
                  <th>Memory Usage</th>
                  <th>Disk Usage</th>
               </tr>
               </thead>
               {postList}
                    
                </table>            
                
   </div> 
   </div>
  )
}
}
export default Table;


