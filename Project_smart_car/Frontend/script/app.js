const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlTemp, htmlInfo, htmlContact;


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

    socket.on('B2F_verstuur_data_JSN1', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-disSens1').innerHTML = `${jsonObject.AfstandJSN1}`
    })

    socket.on('B2F_verstuur_data_JSN2', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-disSens2').innerHTML = `${jsonObject.AfstandJSN2}`
    })

    socket.on('B2F_verstuur_data_JSN3', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-disSens3').innerHTML = `${jsonObject.AfstandJSN3}`
    })

    socket.on('B2F_verstuur_data_JSN4', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-disSens4').innerHTML = `${jsonObject.AfstandJSN4}`
    })

    socket.on('B2F_verstuur_data_speed', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-speed').innerHTML = `${jsonObject.speed} km/h`
    })
  }
 
};

const init = function(){
  htmlTemp = document.querySelector('.js-temperature')
  htmlInfo = document.querySelector('.js-info')
  htmlContact = document.querySelector('.js-contact')

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
