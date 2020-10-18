import React from 'react'
import { Navbar, Nav, Button} from 'react-bootstrap';
import './navbar.css';
import { NavLink, Redirect} from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import axios from 'axios';

import { faChartArea,
    faDesktop,
    faTable,
    faGlobe,
    faFileExcel,
    faLongArrowAltUp
} from '@fortawesome/free-solid-svg-icons';

class Bar extends React.Component{

    handleLogout = () =>{
        axios.get('http://localhost:9000/users/logout')
        .then(response =>{
            console.log(response);
            if(response.status === 200){
                console.log("logout success")
                return (<Redirect to="/"/>)
                
    }
        })
        .catch(err =>{console.log(err)})
    }

    render(){
        return(
            <React.Fragment>
            <Navbar variant="none" className="head">
                <Navbar.Brand href="#home" style={{color:"black", fontFamily:"Segoe UI', Tahoma, Geneva, Verdana, sans-serif", fontWeight:"600"}}>Network Monitoring System</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"/>


                <Navbar.Collapse id="basic-navbar-nav">
                    <NavLink to='/home'><Button variant="outline-info" className="navButton" ><FontAwesomeIcon className="iconDisplay" icon={faDesktop} />  Home</Button></NavLink>
                    <Nav className="ml-auto">

                        <NavLink to='/Top'><Button variant="outline-info" className="navButton"><FontAwesomeIcon className="iconDisplay" icon={faGlobe} />  Processes</Button></NavLink>
                        <NavLink to='/Table'><Button variant="outline-info" className="navButton"><FontAwesomeIcon className="iconDisplay" icon={faTable} />  Tabular View</Button></NavLink>
                        <NavLink to='/Gauge'> <Button variant="outline-info" className="navButton"><FontAwesomeIcon className="iconDisplay" icon={faChartArea} />  Chart View</Button></NavLink>
                        <NavLink to='/Data'> <Button variant="outline-info" className="navButton"><FontAwesomeIcon className="iconDisplay" icon={faFileExcel} />  Export</Button></NavLink>
                        <NavLink to='/'><Button variant="outline-info" className="navButton" onClick={this.handleLogout}><FontAwesomeIcon className="iconDisplay" icon={faLongArrowAltUp} />  Logout</Button></NavLink>
                    </Nav>
                </Navbar.Collapse>
                
            </Navbar>
            </React.Fragment>
        )
    }
}

export default Bar;