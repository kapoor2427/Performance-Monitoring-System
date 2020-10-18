import React from "react";
import CommonNavbar from "./Navbar";
import { Container,Button } from "react-bootstrap";

import { DateRange } from "react-date-range";


function Data() {


  const[dateRange,setdateRange]=React.useState(null);

  

  function handleSelect(startDate,endDate) {


    let sdate = startDate.format("DD-MM-YYYY")
    // let sdate=`${startDate.date()}-${startDate.month()}-${startDate.year()}`

    console.log(sdate)
    let edate = endDate.format("DD-MM-YYYY")
    // let edate=`${endDate.date()}-${endDate.month()}-${endDate.year()}`
    console.log(edate)

    
    let ranges=`startDate=${sdate}&endDate=${edate}`
    console.log(ranges)

    setdateRange(ranges)
  }




  
function openInNewTab() {
  console.log("hello")
    var URL =`http://127.0.0.1:5000/api/data/export?${dateRange}`
  console.log("url",URL)
  var win = window.open(URL, '_blank');
  win.focus();
}

  return (
    <React.Fragment>

    <CommonNavbar/>
    <p></p>
    <Container>
      <DateRange
        // onInit={handleSelect}
        onChange={(event) => handleSelect(event.startDate,event.endDate)}
      />

      <Button variant="secondary" onClick={()=>openInNewTab()}>Export</Button>

</Container>
    </React.Fragment>
  );
}

export default Data;
