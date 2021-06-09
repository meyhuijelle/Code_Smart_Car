const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlTemp, htmlInfo, htmlContact, htmlParkSens, visual1_top, visual2_top, visual3_top, 
visual4_top, visual1_bottom, visual2_bottom, visual3_bottom,visual4_bottom, visual1_right,
visual2_right, visual3_right, visual4_right, visual1_left, visual2_left, visual3_left, 
visual4_left;




// const showHistoriek = function(jsonObject){
//   console.log(jsonObject)
// //   let htmlString = `<tr>
// //   <th>HistoriekID</th>
// //   <th>DeviceID</th>
// //   <th>ActieID</th>
// //   <th>Actiedatum</th>
// //   <th>Waarde</th>
// //   <th>Commentaar</th>
// // </tr>`
// let htmlString = `` 
//   const placeholder = document.querySelector('.js-historiek')
//   for(historiek of jsonObject.historiek){
//     console.log(historiek)
//     // htmlString += `<li class="js-historiek_option">ID: ${historiek.ActieID} ActieDatum: ${historiek.Actiedatum} kies</li>`
//     htmlString += ` <tr>
//     <td>ID: ${historiek.ActieID} --- Actiedatum: ${historiek.Actiedatum} --- Commentaar: ${historiek.Commentaar} --- DeviceID: ${historiek.DeviceID} --- HistoriekID: ${historiek.HistoriekID} </td>
//     </tr>`

    
//   }
//   placeholder.innerHTML = htmlString

// }

const getHistoriek = function(){
  handleData(`http://192.168.168.168:5000/api/v1/historiek`, showHistoriek)
}

const listenToUI = function () {
  // if(htmlTemp){
  //   const homeButton = document.querySelector('.js-homeButton');
  //   homeButton.addEventListener('click', function(){
  //     console.log('Back to home screen!')
  //     window.location.href = 'index.html'
  //   })

  //   const infoButton = document.querySelector('.js-buttonInfo');
  //   infoButton.addEventListener('click', function(){
  //   console.log('***info*** button pushed!')
  //   window.location.href = 'info.html'
  // })
  // const contactButton = document.querySelector('.js-buttonContact');
  // contactButton.addEventListener('click', function(){
  //   console.log('***contact*** button pushed!')
  //   window.location.href = 'contact.html'
  // })
  
  // }
  // if(htmlInfo){
  // const homeButton = document.querySelector('.js-homeButton');
  // homeButton.addEventListener('click', function(){
  //   console.log('Back to home screen!')
  //   window.location.href = 'index.html'
  // })
  // const infoButton = document.querySelector('.js-buttonInfo');
  // infoButton.addEventListener('click', function(){
  //   console.log('***info*** button pushed!')
  //   window.location.href = 'info.html'
  // })
  // const contactButton = document.querySelector('.js-buttonContact');
  // contactButton.addEventListener('click', function(){
  //   console.log('***contact*** button pushed!')
  //   window.location.href = 'contact.html'
  // })
  // } 

  // if(htmlContact){
  // const homeButton = document.querySelector('.js-homeButton');
  // homeButton.addEventListener('click', function(){
  //   console.log('Back to home screen!')
  //   window.location.href = 'index.html'
  // })
  // const infoButton = document.querySelector('.js-buttonInfo');
  // infoButton.addEventListener('click', function(){
  //   console.log('***info*** button pushed!')
  //   window.location.href = 'info.html'
  // })

  // const contactButton = document.querySelector('.js-buttonContact');
  // contactButton.addEventListener('click', function(){
  //   console.log('***contact*** button pushed!')
  //   window.location.href = 'contact.html'
  // })
  // if(htmlTemp){
    if(htmlTemp){
      const contactButton = document.querySelector('.js-buttonContact');
      contactButton.addEventListener('click', function(){
      console.log('***contact*** button pushed!')
      window.location.href = 'contact.html'
    })

    const historyButton = document.querySelector('.js-buttonHistory');
    historyButton.addEventListener('click', function(){
      console.log('***history*** button pushed!')
      window.location.href = 'history.html'
    })

    const parkingSensButton = document.querySelector(".js-parkingSensButton");
    parkingSensButton.addEventListener('click', function(){
      console.log('***parkingSens*** button pushed!')
      window.location.href = 'parkingSens.html'
    })
    }

    if(htmlInfo){
      const contactButton = document.querySelector('.js-buttonContact');
      contactButton.addEventListener('click', function(){
      console.log('***contact*** button pushed!')
      window.location.href = 'contact.html'
    })
  }

  if(htmlContact){
    const contactButton = document.querySelector('.js-buttonContact');
      contactButton.addEventListener('click', function(){
      console.log('***contact*** button pushed!')
      window.location.href = 'contact.html'
    })
  }

    const homeButton = document.querySelector('.js-homeButton');
    homeButton.addEventListener('click', function(){
      console.log('Back to home screen!')
      window.location.href = 'index.html'
    })
    const infoButton = document.querySelector('.js-buttonInfo');
    infoButton.addEventListener('click', function(){
      console.log('***info*** button pushed!')
      window.location.href = 'info.html'
    })
   
    

    // socket.on('B2F_verstuur_data_speed', function(jsonObject){
  //   console.log(jsonObject)
  //   document.querySelector('.js-speed').innerHTML = `${jsonObject.speed} km/h`
  // })
  // }
  
  } 

  


const listenToSocket = function () {
  if(htmlTemp){
    socket.on("connect", function () {
      console.log("verbonden met socket webserver");
    });

    socket.on('B2F_verstuur_data_ldr', function(jsonObject){
      // let today = new Date();
      console.log(jsonObject)
      document.querySelector('.js-brightness').innerHTML = `${jsonObject.lichtsterkte}%`
    }) 
  
    socket.on('B2F_verstuur_data_dallas', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-temperature').innerHTML = `${jsonObject.temperatuur}`
    })
  }
  else if(htmlParkSens){    
    socket.on('B2F_verstuur_data_JSN1', function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-disSens1').innerHTML = `${jsonObject.AfstandJSN1}`
    if(jsonObject.AfstandJSN1 == -1){
      // console.log('neeee');
      visual1_top.classList.remove('c-parking__layoutSM')
      visual2_top.classList.remove('c-parking__layoutMD')
      visual3_top.classList.remove('c-parking__layoutlg')
      visual4_top.classList.remove('c-parking__layoutxl')
      // console.log(visual1_top.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN1 == 0){
      visual1_top.classList.add('c-parking__layoutSM')
      visual2_top.classList.add('c-parking__layoutMD')
      visual3_top.classList.add('c-parking__layoutlg')
      visual4_top.classList.add('c-parking__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    else if(jsonObject.AfstandJSN1 <= 30){
      visual1_top.classList.add('c-parking__layoutSM')
      visual2_top.classList.add('c-parking__layoutMD')
      visual3_top.classList.add('c-parking__layoutlg')
      visual4_top.classList.remove('c-parking__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }else if(jsonObject.AfstandJSN1 <= 50){
      visual1_top.classList.add('c-parking__layoutSM')
      visual2_top.classList.add('c-parking__layoutMD')
      visual3_top.classList.remove('c-parking__layoutlg')
      visual4_top.classList.remove('c-parking__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }else if(jsonObject.AfstandJSN1 > 50){
      visual1_top.classList.add('c-parking__layoutSM')
      visual2_top.classList.remove('c-parking__layoutMD')
      visual3_top.classList.remove('c-parking__layoutlg')
      visual4_top.classList.remove('c-parking__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN2', function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-disSens2').innerHTML = `${jsonObject.AfstandJSN2}`

   
    if(jsonObject.AfstandJSN2 == -1){
      // console.log('neeee');
      visual1_bottom.classList.remove('c-parking__layoutSM2')
      visual2_bottom.classList.remove('c-parking__layoutMD')
      visual3_bottom.classList.remove('c-parking__layoutlg')
      visual4_bottom.classList.remove('c-parking__layoutxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN2 == 0){
      visual1_bottom.classList.add('c-parking__layoutSM2')
      visual2_bottom.classList.add('c-parking__layoutMD')
      visual3_bottom.classList.add('c-parking__layoutlg')
      visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 <= 30){
      visual1_bottom.classList.add('c-parking__layoutSM2')
      visual2_bottom.classList.add('c-parking__layoutMD')
      visual3_bottom.classList.add('c-parking__layoutlg')
      visual4_bottom.classList.remove('c-parking__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 <= 50){
      visual1_bottom.classList.add('c-parking__layoutSM2')
      visual2_bottom.classList.add('c-parking__layoutMD')
      visual3_bottom.classList.remove('c-parking__layoutlg')
      visual4_bottom.classList.remove('c-parking__layoutxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 > 50){
      visual1_bottom.classList.add('c-parking__layoutSM2')
      visual2_bottom.classList.remove('c-parking__layoutMD')
      visual3_bottom.classList.remove('c-parking__layoutlg')
      visual4_bottom.classList.remove('c-parking__layoutxl')
      // visual2_bottom.classList.add('c-parking__layoutMD')
      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN3', function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-disSens3').innerHTML = `${jsonObject.AfstandJSN3}`

    if(jsonObject.AfstandJSN3 == -1){
      // console.log('neeee');
      visual1_right.classList.remove('c-parking__layoutSMHorSM')
      visual2_right.classList.remove('c-parking__layoutHorMD')
      visual3_right.classList.remove('c-parking__layoutHorlg')
      visual4_right.classList.remove('c-parking__layoutHorxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
      

    }
    else if(jsonObject.AfstandJSN3 == 0){
      visual1_right.classList.add('c-parking__layoutSMHorSM')
      visual2_right.classList.add('c-parking__layoutHorMD')
      visual3_right.classList.add('c-parking__layoutHorlg')
      visual4_right.classList.add('c-parking__layoutHorxl')
    }
    
    else if(jsonObject.AfstandJSN3 <= 30){
      visual1_right.classList.add('c-parking__layoutSMHorSM')
      visual2_right.classList.add('c-parking__layoutHorMD')
      visual3_right.classList.add('c-parking__layoutHorlg')
      visual4_right.classList.remove('c-parking__layoutHorxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN3 <= 50){
      visual1_right.classList.add('c-parking__layoutSMHorSM')
      visual2_right.classList.add('c-parking__layoutHorMD')
      visual3_right.classList.remove('c-parking__layoutlg')
      visual4_right.classList.remove('c-parking__layoutHorxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN3 > 50){
      visual1_right.classList.add('c-parking__layoutSMHorSM')
      visual2_right.classList.remove('c-parking__layoutHorMD')
      visual3_right.classList.remove('c-parking__layoutHorlg')
      visual4_right.classList.remove('c-parking__layoutHorxl')
      // visual2_bottom.classList.add('c-parking__layoutMD')
      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN4', function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-disSens4').innerHTML = `${jsonObject.AfstandJSN4}`

    if(jsonObject.AfstandJSN4 == -1){
      // console.log('neeee');
      visual1_left.classList.remove('c-parking__layoutSMHorSM')
      visual2_left.classList.remove('c-parking__layoutHorMD')
      visual3_left.classList.remove('c-parking__layoutHorlg')
      visual4_left.classList.remove('c-parking__layoutHorxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN4 == 0){
      visual1_left.classList.add('c-parking__layoutSMHorSM')
      visual2_left.classList.add('c-parking__layoutHorMD')
      visual3_left.classList.add('c-parking__layoutHorlg')
      visual4_left.classList.add('c-parking__layoutHorxl')
    }
    
    else if(jsonObject.AfstandJSN4 <= 30){
      visual1_left.classList.add('c-parking__layoutSMHorSM')
      visual2_left.classList.add('c-parking__layoutHorMD')
      visual3_left.classList.add('c-parking__layoutHorlg')
      visual4_left.classList.remove('c-parking__layoutHorxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN4 <= 50){
      visual1_left.classList.add('c-parking__layoutSMHorSM')
      visual2_left.classList.add('c-parking__layoutHorMD')
      visual3_left.classList.remove('c-parking__layoutlg')
      visual4_left.classList.remove('c-parking__layoutHorxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN4 > 50){
      visual1_left.classList.add('c-parking__layoutSMHorSM')
      visual2_left.classList.remove('c-parking__layoutHorMD')
      visual3_left.classList.remove('c-parking__layoutHorlg')
      visual4_left.classList.remove('c-parking__layoutHorxl')
      // visual2_bottom.classList.add('c-parking__layoutMD')
      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  
}
 
};

const init = function(){
  htmlTemp = document.querySelector('.js-temperature')
  htmlInfo = document.querySelector('.js-info')
  htmlContact = document.querySelector('.js-contact')
  htmlParkSens = document.querySelector('.js-disSens1')
  visual1_top = document.querySelector('.js-visual1_top')
  visual2_top = document.querySelector('.js-visual2_top')
  visual3_top = document.querySelector('.js-visual3_top')
  visual4_top = document.querySelector('.js-visual4_top')

  visual1_bottom = document.querySelector('.js-visual1_bottom')
  visual2_bottom = document.querySelector('.js-visual2_bottom')
  visual3_bottom = document.querySelector('.js-visual3_bottom')
  visual4_bottom = document.querySelector('.js-visual4_bottom')

  visual1_right = document.querySelector('.js-visual1_right')
  visual2_right = document.querySelector('.js-visual2_right')
  visual3_right = document.querySelector('.js-visual3_right')
  visual4_right = document.querySelector('.js-visual4_right')

  visual1_left = document.querySelector('.js-visual1_left')
  visual2_left = document.querySelector('.js-visual2_left')
  visual3_left = document.querySelector('.js-visual3_left')
  visual4_left = document.querySelector('.js-visual4_left')
  

  // console.log('DOM geladen')
  // if(htmlTemp){
  //   listenToClicksIndex();
  // }
  // else if (htmlInfo){
  //   // listenToClicksInfo();
  //   console.log('jajajajaj')
  // }
  // listenToClicksIndex();
  listenToUI();
  listenToSocket();
}

document.addEventListener("DOMContentLoaded", init);
