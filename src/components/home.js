import React from 'react';
import Navbar from './Navbar'



class Home extends React.Component{
    
            
    render(){
        return(
            <React.Fragment>
                <Navbar/>
                <div class="input-group mb-3" style={{width:"50%", marginTop:"10%", marginLeft:"25%", marginRight:"25%"}} >
                    
                    <input type="text" class="form-control" placeholder="Enter Mac Address" aria-label="mac-address"/>
                    <div class="input-group-append">
                        <span class="input-group-text">10.10.11.10</span>
                    </div>
                    <pre>   </pre>
                    <input type="text" class="form-control" placeholder="Enter Host Name" aria-label="host-name"/>
                    <div class="input-group-append">
                        <span class="input-group-text">@BeanBox</span>
                    </div>
                    <button class="btn btn-primary" style={{marginLeft:"5%"}}>Add</button>
                </div>     
                <table class="table table-hover" style={{width:"70%", marginTop:"10%", marginLeft:"15%", marginRight:"15%", textAlign:"center"}}>
                    <thead>
                        <tr>
                        <th scope="col">Id</th>
                        <th scope="col">Mac Address</th>
                        <th scope="col">Username</th>
                        <th scope="col">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">1</th>
                        <td>10.11.01.1</td>
                        <td>XYZ</td>
                        <td>connected</td>
                        </tr>
                        <tr>
                        <th scope="row">2</th>
                        <td>10.01.01.11</td>
                        <td>ABCD</td>
                        <td>disconnected</td>
                        </tr>
                    </tbody>
                </table>            
                
            </React.Fragment>
        )
    }
}

export default Home;