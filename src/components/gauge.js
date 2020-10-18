import React, { useEffect } from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { Container, Row, Col,Jumbotron } from "react-bootstrap";
import CommonNavbar from './Navbar';


function Gauge() {


  const [systemsInfo, setSystemsInfo] = React.useState(null);



  useEffect(() => {
    setInterval(loadData,5000)
    console.log('in useEffect')
  },[]);

  function loadData()
  {
    var xhr = new XMLHttpRequest();

    xhr.withCredentials=true;

    xhr.open("GET", "http://127.0.0.1:5000/api/data");
    xhr.setRequestHeader("Content-Type", "application/json;-charset=UTF-8");


    xhr.onload = function(e) {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          var myArr = JSON.parse(xhr.responseText);
          setSystemsInfo(myArr.data);
          // console.log(xhr.response);
          console.log(myArr);


        }
      }
  }
    xhr.send();
  }

  return (
    <React.Fragment>
   <CommonNavbar />

   
    <h1 className="headingGauge" align="center">Real Time Monitoring Gauges</h1>

    <hr></hr>
    <Container fluid>
    {systemsInfo && systemsInfo.map(info =>
                      <Jumbotron fluid className="gauge">
                          <h5 align="center" className="mac" style={{ backgroundColor:"white" }}><strong>Mac address=>{info.macAddress}</strong></h5>
      <p></p>
      <p></p>
      <Container >
      <Row>     
      <Col  >
      <ReactSpeedometer
      maxValue={100}  
      value={info.diskUsage}
      currentValueText="Disk Usage: ${value}"   
      needleColor="red"
      startColor="green"
      segments={10}
      endColor="red"
      needleColor="#002b62"
    />
      </Col>
  
      <Col>
      <ReactSpeedometer
      maxValue={100}
      value={info.memoryUsage}
      
      currentValueText="Memory Usage: ${value}"
      needleColor="red"
      startColor="green"
      segments={10}
      endColor="red"
      
      needleColor="#002b62"
    />
      </Col>
      
      <Col>
      <ReactSpeedometer
      maxValue={100}
      value={info.cpuUsageTotal}
      
      currentValueText="CPU Usage Total: ${value}"
      needleColor="red"
      startColor="green"
      segments={10}
      endColor="red"
      
      needleColor="#002b62"
    />
      </Col>
  
       </Row>
       </Container>
       </Jumbotron>

      
   )}

   
</Container>

    </React.Fragment>
    
    );
}

export default Gauge;
