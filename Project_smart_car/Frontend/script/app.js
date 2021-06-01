const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);



const showHistoriek = function(jsonObject){
  console.log(jsonObject)
//   let htmlString = `<tr>
//   <th>HistoriekID</th>
//   <th>DeviceID</th>
//   <th>ActieID</th>
//   <th>Actiedatum</th>
//   <th>Waarde</th>
//   <th>Commentaar</th>
// </tr>`
let htmlString = `` 
  const placeholder = document.querySelector('.js-historiek')
  for(historiek of jsonObject.historiek){
    console.log(historiek)
    // htmlString += `<li class="js-historiek_option">ID: ${historiek.ActieID} ActieDatum: ${historiek.Actiedatum} kies</li>`
    htmlString += ` <tr>
    <td>ID: ${historiek.ActieID} --- Actiedatum: ${historiek.Actiedatum} --- Commentaar: ${historiek.Commentaar} --- DeviceID: ${historiek.DeviceID} --- HistoriekID: ${historiek.HistoriekID} </td>
    </tr>`

    
  }
  placeholder.innerHTML = htmlString

}

const getHistoriek = function(){
  handleData(`http://192.168.168.168:5000/api/v1/historiek`, showHistoriek)
}

const listenToUI = function () {
  
};

const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  

  socket.on('B2F_verstuur_data_ldr', function(jsonObject){
    // let today = new Date();
    console.log(jsonObject)
    document.querySelector('.js-lichtsterkte').innerHTML = `De lichtsterkte van de LDR is: ${jsonObject.lichtsterkte}%`
  }) 

  socket.on('B2F_verstuur_data_dallas', function(jsonObject){
    console.log(jsonObject)
    document.querySelector('.js-temperatuur').innerHTML = `De temperatuur in de wagen bedraagt: ${jsonObject.temperatuur}`
  })

};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  listenToUI();
  listenToSocket();
  getHistoriek();
});
