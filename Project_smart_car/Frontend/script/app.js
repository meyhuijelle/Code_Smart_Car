const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);

let htmlTemp, htmlInfo, htmlContact, htmlParkSens, visual1_top, visual2_top, visual3_top, 
visual4_top, visual1_bottom, visual2_bottom, visual3_bottom,visual4_bottom, visual1_right,
visual2_right, visual3_right, visual4_right, visual1_left, visual2_left, visual3_left, 
visual4_left,htmlHistory;

let tellerLights = 0;
let tellerBuzzer = 0;
let tellerONOFF = 0;




const showHistoriek = function(jsonObject){
  console.log(jsonObject)
  let htmlString = ` 
  <thead>
  <th>historyID</th>
  <th>deviceID</th>
  <th>actionID</th>
  <th>action Date</th>
  <th>value</th>
  <th>commentary</th>
</thead>`
// let htmlString = `` 
  let index = 0
  const placeholder = document.querySelector('.js-history')
  
  for(historiek of jsonObject.historiek){
    console.log(historiek)
    index ++
    if(index % 2 == 0){
      htmlString +=
      ` <tbody>
      <tr class="even">
          <td data-label="historyID">${historiek.HistoriekID}</td>
          <td data-label="deviceID">${historiek.DeviceID}</td>
          <td data-label="actionID">${historiek.ActieID}</td>
          <td data-label="actdate">${historiek.Actiedatum}</td>
          <td data-label="value">${historiek.Waarde}</td>
          <td data-label="commentary">${historiek.Commentaar}</td>
      </tr>
     
  </tbody>`
    }else{
      htmlString +=
      ` <tbody>
      <tr class="odd">
          <td data-label="historyID">${historiek.HistoriekID}</td>
          <td data-label="deviceID">${historiek.DeviceID}</td>
          <td data-label="actionID">${historiek.ActieID}</td>
          <td data-label="actdate">${historiek.Actiedatum}</td>
          <td data-label="value">${historiek.Waarde}</td>
          <td data-label="commentary">${historiek.Commentaar}</td>
      </tr>
     
  </tbody>`
    }
    
    // htmlString += `<li class="js-historiek_option">ID: ${historiek.ActieID} ActieDatum: ${historiek.Actiedatum} kies</li>`


    
  }
  placeholder.innerHTML = htmlString

}

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

    const buttonbuzzerONOFF = document.querySelector('.js-buttonBuzzerONOFF');
    let htmlString1 = ""
    buttonbuzzerONOFF.addEventListener('click', function(){
      console.log('Er is op me gedrukt!')

      tellerBuzzer++

      console.log(tellerBuzzer)
      
      if(tellerBuzzer == 1){
          // console.log(buttonONOFF.classList)
          htmlString1 = `<div class="c-button c-button__clicked js-statebuzzer" state="True">
          <div>
          <svg id="volume_up_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path id="Path_16" data-name="Path 16" d="M0,0H24V24H0Z" fill="none"/>
          <path id="Path_17" data-name="Path 17" d="M3,9v6H7l5,5V4L7,9Zm13.5,3A4.5,4.5,0,0,0,14,7.97v8.05A4.474,4.474,0,0,0,16.5,12ZM14,3.23V5.29a7,7,0,0,1,0,13.42v2.06A8.994,8.994,0,0,0,14,3.23Z" fill="#4d00b3"/>
        </svg>
        

          </div>
          <div>
              <p class="u-mb-clear">BUZZER</p>
              <p class="u-mb-clear"><u>ON</u>/OFF</u></p>
          </div>
      </div>`
      }else{
        htmlString1 = `
        <div class="c-button js-statebuzzer" state="False">
          <div>
              <svg id="volume_off_black_24dp_1_" data-name="volume_off_black_24dp (1)" xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                  viewBox="0 0 24 24">
                  <path id="Path_30" data-name="Path 30" d="M0,0H24V24H0Z" fill="none" />
                  <path id="Path_31" data-name="Path 31"
                      d="M16.5,12A4.5,4.5,0,0,0,14,7.97v2.21l2.45,2.45A4.232,4.232,0,0,0,16.5,12ZM19,12a6.843,6.843,0,0,1-.54,2.64l1.51,1.51A8.8,8.8,0,0,0,21,12a9,9,0,0,0-7-8.77V5.29A7.005,7.005,0,0,1,19,12ZM4.27,3,3,4.27,7.73,9H3v6H7l5,5V13.27l4.25,4.25A6.924,6.924,0,0,1,14,18.7v2.06a8.99,8.99,0,0,0,3.69-1.81L19.73,21,21,19.73l-9-9ZM12,4,9.91,6.09,12,8.18Z" />
              </svg>

          </div>
          <div>
              <p class="u-mb-clear">BUZZER</p>
              <p class="u-mb-clear"> ON/<u>OFF</u></p>
          </div>
      </div>
  `
  tellerBuzzer = 0

      }
      buttonbuzzerONOFF.innerHTML = htmlString1;

      const state = document.querySelector('.js-statebuzzer')
      const value = state.getAttribute('state')
      console.log(value)
      socket.emit('F2B_stateBuzzer', {stateBuzzer: state.getAttribute('state')});
    })
    
    

  
    const buttonLightsONOFF = document.querySelector('.js-buttonLightsONOFF');
    
    let htmlString2 = ""
    buttonLightsONOFF.addEventListener('click', function(){
      console.log('Er is op me gedrukt!')

      tellerLights++

      console.log(tellerLights)
      
      if(tellerLights == 1){
          // console.log(buttonONOFF.classList)
          htmlString2 = `<div class="c-button c-button__clicked js-buttonLightsONOFF js-stateLights" state="True">
        <div>
           

            <svg xmlns="http://www.w3.org/2000/svg" width="31.591" height="24" viewBox="0 0 31.591 24">
        <g id="Group_484" data-name="Group 484" transform="translate(-262.046 -543)">
          <g id="lightbulb_black_24dp" transform="translate(266 543)">
            <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none"/>
            <path id="Path_19" data-name="Path 19" d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" fill="#4d00b3"/>
          </g>
          <line id="Line_15" data-name="Line 15" y1="2" x2="6" transform="translate(286.5 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_16" data-name="Line 16" x2="4" transform="translate(287 552)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_17" data-name="Line 17" x2="7" y2="2" transform="translate(286.5 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_18" data-name="Line 18" x1="5.303" y1="2" transform="translate(263.197 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_19" data-name="Line 19" x1="4" transform="translate(264 552)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_20" data-name="Line 20" x1="6.303" y2="2" transform="translate(262.197 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
        </g>
      </svg>

        </div>
        <div>
            <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS <u>ON</u>/OFF</u></p>
        </div>
    </div>`
      }else{
        htmlString2 = `
        <div class="c-button js-buttonLightsONOFF js-stateLights" state="False">
        <div>
        <svg id="lightbulb_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none" />
                <path id="Path_19" data-name="Path 19"
                    d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" />
            </svg>
      
        </div>
        <div>
            <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS ON/<u>OFF</u></p>
        </div>
    </div>
  `
  tellerLights = 0

      }
      buttonLightsONOFF.innerHTML = htmlString2;
      const state = document.querySelector('.js-stateLights')
      const value = state.getAttribute('state')
      console.log(value)
      socket.emit('F2B_stateLights', {stateLights: state.getAttribute('state')});

      
  //       if(value == false && jsonObject.state == "True"){
  //         htmlString2 = `<div class="c-button c-button__clicked js-buttonLightsONOFF js-state" state="True">
  //       <div>
           

  //           <svg xmlns="http://www.w3.org/2000/svg" width="31.591" height="24" viewBox="0 0 31.591 24">
  //       <g id="Group_484" data-name="Group 484" transform="translate(-262.046 -543)">
  //         <g id="lightbulb_black_24dp" transform="translate(266 543)">
  //           <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none"/>
  //           <path id="Path_19" data-name="Path 19" d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" fill="#4d00b3"/>
  //         </g>
  //         <line id="Line_15" data-name="Line 15" y1="2" x2="6" transform="translate(286.5 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
  //         <line id="Line_16" data-name="Line 16" x2="4" transform="translate(287 552)" fill="none" stroke="#707070" stroke-width="1"/>
  //         <line id="Line_17" data-name="Line 17" x2="7" y2="2" transform="translate(286.5 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
  //         <line id="Line_18" data-name="Line 18" x1="5.303" y1="2" transform="translate(263.197 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
  //         <line id="Line_19" data-name="Line 19" x1="4" transform="translate(264 552)" fill="none" stroke="#707070" stroke-width="1"/>
  //         <line id="Line_20" data-name="Line 20" x1="6.303" y2="2" transform="translate(262.197 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
  //       </g>
  //     </svg>

  //       </div>
  //       <div>
  //           <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS <u>ON</u>/OFF</u></p>
  //       </div>
  //   </div>`
  //       }else if(value == true && jsonObject.state == "False"){
  //         htmlString2 = `
  //       <div class="c-button js-buttonLightsONOFF js-state" state="False">
  //       <div>
  //       <svg id="lightbulb_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
  //               <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none" />
  //               <path id="Path_19" data-name="Path 19"
  //                   d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" />
  //           </svg>
      
  //       </div>
  //       <div>
  //           <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS ON/<u>OFF</u></p>
  //       </div>
  //   </div>
  // `
  //       }

       

   
      buttonLightsONOFF.innerHTML = htmlString2;

    })

      
    const buttonONOFF = document.querySelector('.js-buttonONOFF');
    let htmlString3 = ""
    buttonONOFF.addEventListener('click', function(){
      console.log('Er is op me gedrukt!')

      tellerONOFF++

      console.log(tellerONOFF)
      
      if(tellerONOFF == 1){
          // console.log(buttonONOFF.classList)
          htmlString3 = `<div class="c-button">
          <div>
          <svg id="power_settings_new_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
          <path id="Path_10" data-name="Path 10" d="M0,0H24V24H0Z" fill="none"/>
          <path id="Path_11" data-name="Path 11" d="M13,3H11V13h2Zm4.83,2.17L16.41,6.59A6.92,6.92,0,0,1,19,12,7,7,0,1,1,7.58,6.58L6.17,5.17A8.992,8.992,0,1,0,21,12,8.932,8.932,0,0,0,17.83,5.17Z"/>
        </svg>
        


          </div>
          <div>
              <p class="c-text__layout-btn u-mb-clear">APPLICATION ON/<u>OFF</u></p>
          </div>
      </div>`
      }else{
        htmlString3 = `
        <div class="c-button c-button__clicked">
        <div>
            <svg id="power_settings_new_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                <path id="Path_10" data-name="Path 10" d="M0,0H24V24H0Z" fill="none" />
                <path id="Path_11" data-name="Path 11"
                    d="M13,3H11V13h2Zm4.83,2.17L16.41,6.59A6.92,6.92,0,0,1,19,12,7,7,0,1,1,7.58,6.58L6.17,5.17A8.992,8.992,0,1,0,21,12,8.932,8.932,0,0,0,17.83,5.17Z"
                    fill="#4d00b3" />
            </svg>


        </div>
        <div>
            <p class="c-text__layout-btn u-mb-clear">APPLICATION <u>ON</u>/OFF</p>
        </div>
    </div>
  `
  tellerONOFF = 0

      }
      buttonONOFF.innerHTML = htmlString3;
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
   
    
} 

  


const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  if(htmlTemp){
    socket.on('B2F_verstuur_data_ldr', function(jsonObject){
      // let today = new Date();
      console.log(jsonObject)
      document.querySelector('.js-brightness').innerHTML = `${jsonObject.lichtsterkte}%`
    }) 
  
    socket.on('B2F_verstuur_data_dallas', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-temperature').innerHTML = `${jsonObject.temperatuur}`
    })

    socket.on('B2F_verstuur_data_speed', function(jsonObject){
      console.log(jsonObject)
      document.querySelector('.js-speed').innerHTML = `${jsonObject.speed} km/h`
    })

    socket.on("B2F_state_with_button", function (jsonObject) {
      // console.log(jsonObject.state);

      const buttonLightsONOFF = document.querySelector('.js-buttonLightsONOFF');
    
      let htmlString2 = ""
     
      console.log(tellerLights)

      tellerLights = jsonObject.state

      console.log(tellerLights)
      
      if(tellerLights == 1){
          // console.log(buttonONOFF.classList)
          htmlString2 = `<div class="c-button c-button__clicked js-buttonLightsONOFF js-stateLights" state="True">
        <div>
          

            <svg xmlns="http://www.w3.org/2000/svg" width="31.591" height="24" viewBox="0 0 31.591 24">
        <g id="Group_484" data-name="Group 484" transform="translate(-262.046 -543)">
          <g id="lightbulb_black_24dp" transform="translate(266 543)">
            <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none"/>
            <path id="Path_19" data-name="Path 19" d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" fill="#4d00b3"/>
          </g>
          <line id="Line_15" data-name="Line 15" y1="2" x2="6" transform="translate(286.5 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_16" data-name="Line 16" x2="4" transform="translate(287 552)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_17" data-name="Line 17" x2="7" y2="2" transform="translate(286.5 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_18" data-name="Line 18" x1="5.303" y1="2" transform="translate(263.197 545.5)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_19" data-name="Line 19" x1="4" transform="translate(264 552)" fill="none" stroke="#707070" stroke-width="1"/>
          <line id="Line_20" data-name="Line 20" x1="6.303" y2="2" transform="translate(262.197 555.5)" fill="none" stroke="#707070" stroke-width="1"/>
        </g>
      </svg>

        </div>
        <div>
            <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS <u>ON</u>/OFF</u></p>
        </div>
    </div>`
      }else{
        htmlString2 = `
        <div class="c-button js-buttonLightsONOFF js-stateLights" state="False">
        <div>
        <svg id="lightbulb_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none" />
                <path id="Path_19" data-name="Path 19"
                    d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" />
            </svg>
      
        </div>
        <div>
            <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS ON/<u>OFF</u></p>
        </div>
    </div>
  `
    tellerLights = 0

        }
        buttonLightsONOFF.innerHTML = htmlString2;



      });
  
}
  else if(htmlParkSens){    
    socket.on('B2F_verstuur_data_JSN1', function(jsonObject){
    console.log(jsonObject)
    // document.querySelector('.js-disSens1').innerHTML = `${jsonObject.AfstandJSN1}`
    if(jsonObject.AfstandJSN1 == -1){
      // console.log('neeee');
      visual1_top.classList.remove('c-color__layoutSM')
      visual2_top.classList.remove('c-color__layoutMD')
      visual3_top.classList.remove('c-color__layoutlg')
      visual4_top.classList.remove('c-color__layoutxl')
      // console.log(visual1_top.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN1 == 0){
      visual1_top.classList.add('c-color__layoutSM')
      visual2_top.classList.add('c-color__layoutMD')
      visual3_top.classList.add('c-color__layoutlg')
      visual4_top.classList.add('c-color__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    else if(jsonObject.AfstandJSN1 <= 30){
      visual1_top.classList.add('c-color__layoutSM')
      visual2_top.classList.add('c-color__layoutMD')
      visual3_top.classList.add('c-color__layoutlg')
      visual4_top.classList.remove('c-color__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }else if(jsonObject.AfstandJSN1 <= 50){
      visual1_top.classList.add('c-color__layoutSM')
      visual2_top.classList.add('c-color__layoutMD')
      visual3_top.classList.remove('c-color__layoutlg')
      visual4_top.classList.remove('c-color__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }else if(jsonObject.AfstandJSN1 > 50){
      visual1_top.classList.add('c-color__layoutSM')
      visual2_top.classList.remove('c-color__layoutMD')
      visual3_top.classList.remove('c-color__layoutlg')
      visual4_top.classList.remove('c-color__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN2', function(jsonObject){
    console.log(jsonObject)
    // document.querySelector('.js-disSens2').innerHTML = `${jsonObject.AfstandJSN2}`

   
    if(jsonObject.AfstandJSN2 == -1){
      // console.log('neeee');
      visual1_bottom.classList.remove('c-color__layoutSM2')
      visual2_bottom.classList.remove('c-color__layoutMD')
      visual3_bottom.classList.remove('c-color__layoutlg')
      visual4_bottom.classList.remove('c-color__layoutxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN2 == 0){
      visual1_bottom.classList.add('c-color__layoutSM2')
      visual2_bottom.classList.add('c-color__layoutMD')
      visual3_bottom.classList.add('c-color__layoutlg')
      visual4_bottom.classList.add('c-color__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 <= 30){
      visual1_bottom.classList.add('c-color__layoutSM2')
      visual2_bottom.classList.add('c-color__layoutMD')
      visual3_bottom.classList.add('c-color__layoutlg')
      visual4_bottom.classList.remove('c-color__layoutxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 <= 50){
      visual1_bottom.classList.add('c-color__layoutSM2')
      visual2_bottom.classList.add('c-color__layoutMD')
      visual3_bottom.classList.remove('c-color__layoutlg')
      visual4_bottom.classList.remove('c-color__layoutxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN2 > 50){
      visual1_bottom.classList.add('c-color__layoutSM2')
      visual2_bottom.classList.remove('c-color__layoutMD')
      visual3_bottom.classList.remove('c-color__layoutlg')
      visual4_bottom.classList.remove('c-color__layoutxl')
      // visual2_bottom.classList.add('c-parking__layoutMD')
      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN3', function(jsonObject){
    console.log(jsonObject)
    // document.querySelector('.js-disSens3').innerHTML = `${jsonObject.AfstandJSN3}`

    if(jsonObject.AfstandJSN3 == -1){
      // console.log('neeee');
      visual1_right.classList.remove('c-color__layoutSMHorSM')
      visual2_right.classList.remove('c-color__layoutSMHorMD')
      visual3_right.classList.remove('c-color__layoutSMHorlg')
      visual4_right.classList.remove('c-color__layoutSMHorxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
      

    }
    else if(jsonObject.AfstandJSN3 == 0){
      visual1_right.classList.add('c-color__layoutSMHorSM')
      visual2_right.classList.add('c-color__layoutSMHorMD')
      visual3_right.classList.add('c-color__layoutSMHorlg')
      visual4_right.classList.add('c-color__layoutSMHorxl')
    }
    
    else if(jsonObject.AfstandJSN3 <= 30){
      visual1_right.classList.add('c-color__layoutSMHorSM')
      visual2_right.classList.add('c-color__layoutSMHorMD')
      visual3_right.classList.add('c-color__layoutSMHorlg')
      visual4_right.classList.remove('c-color__layoutSMHorxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN3 <= 50){
      visual1_right.classList.add('c-color__layoutSMHorSM')
      visual2_right.classList.add('c-color__layoutSMHorMD')
      visual3_right.classList.remove('c-color__layoutSMHorlg')
      visual4_right.classList.remove('c-color__layoutSMHorxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN3 > 50){
      visual1_right.classList.add('c-color__layoutSMHorSM')
      visual2_right.classList.remove('c-color__layoutSMHorMD')
      visual3_right.classList.remove('c-color__layoutSMHorlg')
      visual4_right.classList.remove('c-color__layoutSMHorxl')
      // visual2_bottom.classList.add('c-parking__layoutMD')
      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
  })

  socket.on('B2F_verstuur_data_JSN4', function(jsonObject){
    console.log(jsonObject)
    // document.querySelector('.js-disSens4').innerHTML = `${jsonObject.AfstandJSN4}`

    if(jsonObject.AfstandJSN4 == -1){
      // console.log('neeee');
      visual1_left.classList.remove('c-color__layoutSMHorSM')
      visual2_left.classList.remove('c-color__layoutSMHorMD')
      visual3_left.classList.remove('c-color__layoutSMHorlg')
      visual4_left.classList.remove('c-color__layoutSMHorxl')

      // console.log(visual1_bottom.classList)
      // console.log(visual2_top.classList)
      // console.log(visual3_top.classList)
      // console.log(visual4_top.classList)
    }else if(jsonObject.AfstandJSN4 == 0){
      visual1_left.classList.add('c-color__layoutSMHorSM')
      visual2_left.classList.add('c-color__layoutSMHorMD')
      visual3_left.classList.add('c-color__layoutSMHorlg')
      visual4_left.classList.add('c-color__layoutSMHorxl')
    }
    
    else if(jsonObject.AfstandJSN4 <= 30){
      visual1_left.classList.add('c-color__layoutSMHorSM')
      visual2_left.classList.add('c-color__layoutSMHorMD')
      visual3_left.classList.add('c-color__layoutSMHorlg')
      visual4_left.classList.remove('c-color__layoutSMHorxl')

      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN4 <= 50){
      visual1_left.classList.add('c-color__layoutSMHorSM')
      visual2_left.classList.add('c-color__layoutSMHorMD')
      visual3_left.classList.remove('c-color__layoutSMHorlg')
      visual4_left.classList.remove('c-color__layoutSMHorxl')

      // visual3_bottom.classList.add('c-parking__layoutlg')
      // visual4_bottom.classList.add('c-parking__layoutxl')
    }
    
    else if(jsonObject.AfstandJSN4 > 50){
      visual1_left.classList.add('c-color__layoutSMHorSM')
      visual2_left.classList.remove('c-color__layoutSMHorMD')
      visual3_left.classList.remove('c-color__layoutSMHorlg')
      visual4_left.classList.remove('c-color__layoutSMHorxl')
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
  // htmlParkSens = document.querySelector('.js-disSens1')
  htmlParkSens = document.querySelector('.js-disSens')
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

  htmlHistory = document.querySelector('.js-history')
  

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

  if(htmlHistory){
    getHistoriek();
  }

}

document.addEventListener("DOMContentLoaded", init);
