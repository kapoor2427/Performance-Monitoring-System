import React, { Component, useEffect } from "react";

import "./landing.css";

import { Redirect } from "react-router";
import 'jquery-ajax';
import 'popper.js';
import 'jquery';
import image1 from './Social-Media-Monitoring-Tools.jpg';

import {
  Carousel,
  Button,
  Container,
  Navbar,
  Row,
  Col,
  Image,
  Jumbotron,
  Form,
  Modal,
  Nav
} from "react-bootstrap";

var auth;


function MyVerticallyCenteredModal(props) {
  const [username, setusername] = React.useState(null);
  const [password, setpassword] = React.useState(null);
  const [status, setStatus] = React.useState(false);
  const [red, setred] = React.useState(false);

  const [authType] = React.useState("admin");

  useEffect(() => {
    if (status !== false) {
      var data = JSON.stringify({
        username: username,
        password: password
      });

      console.log(data);

      var xhr = new XMLHttpRequest();
      xhr.withCredentials = true;

      xhr.addEventListener("readystatechange", function() {
        if (xhr.readyState === 4) {
          var myArr = JSON.parse(xhr.responseText);

          console.log("myarr", myArr);
            console.log(myArr.code);
            auth = authType;

          setStatus(false);

          if (myArr.code === 200) {
            props.onHide();

            setred(true);
          }
          if(myArr.code != 200){
            alert("Wrong Credentials")
          }
        }
      });

        xhr.open("POST", "http://127.0.0.1:5000/api/auth/admin");
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.setRequestHeader("cache-control", "no-cache");
      xhr.setRequestHeader(
        "Postman-Token",
        "1947c2b0-87ef-4ad0-bb4c-db51cbbac1ee"
      );
      xhr.send(data);
    }
  }, [status]);

  if (red === true) {
    return <Redirect to="/Home" authType={authType} />;
  }

  return (
    <React.Fragment>
      <Modal
        {...props}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header className="mheader" closeButton>
          <Modal.Title id="contained-modal-title-vcenter">
            Admin Login
          </Modal.Title>
        </Modal.Header>
        <Modal.Body className="mbody">
          <Form>
            <Form.Group controlId="formBasicName">
              <Form.Label>User Name</Form.Label>
              <Form.Control
                name="username"
                type="text"
                placeholder="UserName"
                onChange={event => setusername(event.target.value)}
              />
              <Form.Text className="text-muted">Enter Username</Form.Text>
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                name="password"
                placeholder="Password"
                onChange={event => setpassword(event.target.value)}
              />
            </Form.Group>
            <Button onClick={() => setStatus(true)} variant="primary" block>
              Submit
            </Button>
          </Form>
        </Modal.Body>
        <Modal.Footer className="footer">
          <Button onClick={props.onHide}>Close</Button>
        </Modal.Footer>
      </Modal>
    </React.Fragment>
  );
}


function Landing() {
  const [modalShow, setModalShow] = React.useState(false);

  const [modalShowr, setModalShowr] = React.useState(false);

  return (
  <div>

            <nav className="navbar navbar-expand-lg navbar-light" style={{ boxShadow: "0 2px 4px 0 rgba(0, 0, 0, 0.1)"}}>
                <span className="navbar-brand" style={{fontWeight:"700", fontFamily:"Cambria, Cochin, Georgia, Times, 'Times New Roman', serif", fontSize:"40px", marginLeft:"150px", boxSizing:"border-box"}}>Shark Cop</span>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavDropdown">
                    <ul className="navbar-nav ml-auto">
                       <li className="navContent" style={{marginRight:"20px"}}>
                            <button className="btn btn-primary my-2 my-sm-0" data-toggle="modal" data-target="#loginModal" style={{fontWeight:"bold"}} onClick={() => setModalShow(true)}>Admin<span className="sr-only">(current)</span></button>
                            <MyVerticallyCenteredModal
                              show={modalShow}
                              onHide={() => setModalShow(false)}
                            />
                      </li>
                        <li className="navContent" style={{marginRight:"140px"}}>
                            <button className="btn btn-outline-primary my-2 my-sm-0" data-toggle="modal" data-target="#" style={{fontWeight:"bold"}}>About</button>
                        </li>
                    </ul>
                </div>
            </nav>
                

                <div className="container">
                    <div className="row">
                        <div className="col-lg-8">
                            <div id="carouselExampleIndicators" className="carousel slide" data-ride="carousel" style={{width:"90%", margin:"80px 0px 0px 0px", boxShadow: "2px 4px 4px 2px rgba(0, 0, 0, 0.1)", borderRadius:"10px"}}>
                                <ol className="carousel-indicators">
                                    <li data-target="#carouselExampleIndicators" data-slide-to="0" className="active"></li>
                                    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                                </ol>
                                <div className="carousel-inner">
                                    <div className="carousel-item active">
                                        <img className="d-block w-100" src={image1} alt="First slide" style={{borderRadius:"10px"}}/>
                                    </div>
                                    <div className="carousel-item">
                                        <img className="d-block w-100" src={image1} alt="Second slide" style={{borderRadius:"10px"}}/>
                                    </div>
                                    <div className="carousel-item">
                                        <img className="d-block w-100" src={image1} alt="Third slide" style={{borderRadius:"10px"}}/>
                                    </div>
                                </div>
                                <a className="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                                    <span className="sr-only">Previous</span>
                                </a>
                                <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                                    <span className="sr-only">Next</span>
                                </a>
                            </div>
                        </div>
                        <div className="col-sm-4">
                        <div style={{margin:"80px 0px 0  0px", width:"100%"}}>
                            <h2 style={{textAlign:"left", fontSize:"40px", lineHeight:"50px", fontFamily:"Cambria, Cochin, Georgia, Times, 'Times New Roman', serif"}}>Performance And Maintainance Made Easy</h2>
                            <p style={{fontFamily: "Verdana, Geneva, Tahoma, sans-serif", fontWeight:"400"}}><i>We help you gain instant insights into your system’s availability and performance so that you can outsmart competition with an amazing end-user experience.</i></p>
                            <button type="button" className="btn btn-primary" data-toggle="modal" data-target="#loginModal" style={{margin:"20px 0 0 0"}} onClick={() => setModalShow(true)}>Get Started</button>
                        </div>
                        </div>
                    </div>
                </div>

  </div>
  );
}
export { auth };
export default Landing;

